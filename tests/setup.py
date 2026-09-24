"""Download and prepare the complete MNIST dataset.

The script stores the four IDX files in ``data/raw`` and removes the
compressed archives after extraction. It uses only Python's standard library.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import shutil
import struct
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


BASE_URL = "https://storage.googleapis.com/cvdf-datasets/mnist/"


@dataclass(frozen=True)
class Resource:
    archive_name: str
    extracted_name: str
    archive_md5: str
    extracted_md5: str
    count: int
    images: bool


RESOURCES = (
    Resource(
        archive_name="train-images-idx3-ubyte.gz",
        extracted_name="train-images-idx3-ubyte",
        archive_md5="f68b3c2dcbeaaa9fbdd348bbdeb94873",
        extracted_md5="6bbc9ace898e44ae57da46a324031adb",
        count=60_000,
        images=True,
    ),
    Resource(
        archive_name="train-labels-idx1-ubyte.gz",
        extracted_name="train-labels-idx1-ubyte",
        archive_md5="d53e105ee54ea40749a09fcbcd1e9432",
        extracted_md5="a25bea736e30d166cdddb491f175f624",
        count=60_000,
        images=False,
    ),
    Resource(
        archive_name="t10k-images-idx3-ubyte.gz",
        extracted_name="t10k-images-idx3-ubyte",
        archive_md5="9fb629c4189551a2d022fa330f9573f3",
        extracted_md5="2646ac647ad5339dbf082846283269ea",
        count=10_000,
        images=True,
    ),
    Resource(
        archive_name="t10k-labels-idx1-ubyte.gz",
        extracted_name="t10k-labels-idx1-ubyte",
        archive_md5="ec29112dd5afa0611ce80d1b7f02629c",
        extracted_md5="27ae3e4e09519cfbb04c329615203637",
        count=10_000,
        images=False,
    ),
)


def file_md5(path: Path) -> str:
    """Return the MD5 digest of a file without loading it into memory."""
    digest = hashlib.md5()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_idx(path: Path, resource: Resource) -> None:
    """Validate the IDX header, shape, and expected byte count."""
    header_size = 16 if resource.images else 8
    with path.open("rb") as file:
        header = file.read(header_size)

    if len(header) != header_size:
        raise ValueError(f"{path.name} is truncated")

    magic, count = struct.unpack(">II", header[:8])
    expected_magic = 2051 if resource.images else 2049
    if magic != expected_magic or count != resource.count:
        raise ValueError(
            f"{path.name} has invalid header: magic={magic}, count={count}"
        )

    if resource.images:
        rows, columns = struct.unpack(">II", header[8:16])
        if (rows, columns) != (28, 28):
            raise ValueError(f"{path.name} has invalid shape: {rows}x{columns}")
        expected_size = header_size + resource.count * rows * columns
    else:
        expected_size = header_size + resource.count

    actual_size = path.stat().st_size
    if actual_size != expected_size:
        raise ValueError(
            f"{path.name} has invalid size: {actual_size} bytes "
            f"(expected {expected_size})"
        )


def is_valid(path: Path, resource: Resource, *, compressed: bool = False) -> bool:
    """Return whether an archive or extracted file is complete and valid."""
    if not path.is_file():
        return False

    expected_md5 = resource.archive_md5 if compressed else resource.extracted_md5
    try:
        if file_md5(path) != expected_md5:
            return False
        if not compressed:
            validate_idx(path, resource)
    except (OSError, ValueError, struct.error):
        return False
    return True


def remove_if_exists(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def download_archive(resource: Resource, archive_path: Path) -> None:
    """Download one archive atomically and verify its checksum."""
    partial_path = archive_path.with_name(f"{archive_path.name}.part")
    remove_if_exists(partial_path)
    url = f"{BASE_URL}{resource.archive_name}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "alcene-mnist-setup/1.0"},
    )

    try:
        print(f"Downloading {resource.archive_name} ...", flush=True)
        with urllib.request.urlopen(request, timeout=60) as response:
            with partial_path.open("wb") as output:
                shutil.copyfileobj(response, output)

        if not is_valid(partial_path, resource, compressed=True):
            raise ValueError(f"Checksum validation failed for {resource.archive_name}")
        partial_path.replace(archive_path)
    finally:
        remove_if_exists(partial_path)


def extract_archive(resource: Resource, archive_path: Path, target_path: Path) -> None:
    """Extract one archive atomically and verify the resulting IDX file."""
    partial_path = target_path.with_name(f"{target_path.name}.part")
    remove_if_exists(partial_path)

    try:
        print(f"Extracting {resource.archive_name} ...", flush=True)
        with gzip.open(archive_path, "rb") as source:
            with partial_path.open("wb") as output:
                shutil.copyfileobj(source, output)

        if not is_valid(partial_path, resource):
            raise ValueError(f"Validation failed for {resource.extracted_name}")
        partial_path.replace(target_path)
    finally:
        remove_if_exists(partial_path)


def prepare_resource(resource: Resource, raw_dir: Path) -> None:
    """Ensure one extracted IDX file exists, then remove its archive."""
    archive_path = raw_dir / resource.archive_name
    target_path = raw_dir / resource.extracted_name

    if is_valid(target_path, resource):
        print(f"Keeping {resource.extracted_name}")
        remove_if_exists(archive_path)
        return

    if is_valid(archive_path, resource, compressed=True):
        print(f"Using cached {resource.archive_name}")
    else:
        remove_if_exists(archive_path)
        download_archive(resource, archive_path)

    extract_archive(resource, archive_path, target_path)
    remove_if_exists(archive_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download, extract, and clean up the MNIST dataset."
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data",
        help="Dataset root (default: repository data directory)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data_dir: Path = args.data_dir.expanduser()
    if not data_dir.is_absolute():
        data_dir = Path.cwd() / data_dir
    raw_dir = data_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    try:
        for resource in RESOURCES:
            prepare_resource(resource, raw_dir)
    except (OSError, ValueError, urllib.error.URLError) as error:
        print(f"MNIST setup failed: {error}", file=sys.stderr)
        return 1

    print(f"MNIST ready at {raw_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
