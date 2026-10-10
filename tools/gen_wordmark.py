#!/usr/bin/env python3
"""
Bake the alcene.ai wordmark into a 128x64 SSD1306 framebuffer.

The editable master is docs/static/wordmark.svg (128x64, black background,
white paths). The source of truth for the firmware is
docs/static/wordmark_128x64.png -- an exact 128x64 raster of that SVG. This
script thresholds it to 1-bit and emits src/alcene_wordmark.h.

The art is full-frame BY DESIGN: layout, spacing and margins live in the SVG.
This script must NOT crop, re-centre, or rescale -- it converts pixels, nothing
more. (The previous wordmark needed ink-bbox centring because its export had
asymmetric padding; this one does not.)

Threshold is 128, the midpoint. The Edge raster is nearly pure black/white
with only a thin anti-aliased fringe (~300 grey pixels), so the cut point is
not load-bearing the way it was for the Figma export.

Re-rendering the PNG from the SVG (Edge headless, exact 128x64 viewport):

    msedge --headless --disable-gpu --hide-scrollbars --window-size=128,64 \
        --screenshot=docs/static/wordmark_128x64.png \
        file:///.../render.html

where render.html wraps the SVG in a zero-margin 128x64 page. Any SVG
rasteriser that produces an exact 128x64 black-background render works.

Usage:
    python tools/gen_wordmark.py            # header + preview
    python tools/gen_wordmark.py --check    # layout report only
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

PANEL_W, PANEL_H = 128, 64
THRESHOLD = 128

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = ROOT / "docs" / "static" / "wordmark_128x64.png"

OUT_HEADER = ROOT / "src" / "alcene_wordmark.h"
OUT_PNG = ROOT / "docs" / "static" / "wordmark_oled.png"


def load_panel(source: Path) -> Image.Image:
    """Threshold the 128x64 render to 1-bit. No crop, no centre, no scale."""
    img = Image.open(source).convert("L")
    if img.size != (PANEL_W, PANEL_H):
        raise SystemExit(
            f"source is {img.width}x{img.height}, expected "
            f"{PANEL_W}x{PANEL_H} -- re-render from the SVG, do not rescale here"
        )
    return img.point(lambda v: 255 if v >= THRESHOLD else 0)


def to_c_header(panel: Image.Image) -> str:
    """Emit a 128-wide bitmap. 128/8 = 16 bytes per row, no row padding needed."""
    px = panel.load()
    lines = [
        "#pragma once",
        "",
        "// GENERATED FILE -- do not edit by hand.",
        "// Source : docs/static/wordmark_128x64.png",
        "// Master : docs/static/wordmark.svg",
        f"// Target : {PANEL_W}x{PANEL_H} 1-bit SSD1306 framebuffer",
        "",
        "#include <Arduino.h>",
        "",
        f"#define ALCENE_WORDMARK_W {PANEL_W}",
        f"#define ALCENE_WORDMARK_H {PANEL_H}",
        "",
        "// One byte = 8 horizontal pixels, most-significant bit leftmost.",
        "static const uint8_t ALCENE_WORDMARK[] PROGMEM = {",
    ]
    for y in range(PANEL_H):
        row = []
        for x in range(0, PANEL_W, 8):
            byte = 0
            for bit in range(8):
                if px[x + bit, y]:
                    byte |= 1 << (7 - bit)
            row.append(byte)
        lines.append("    " + ", ".join(f"0x{b:02X}" for b in row) + ",")
    lines.append("};")
    lines.append("")
    return "\n".join(lines)


def report(panel: Image.Image) -> None:
    bbox = panel.getbbox()
    if bbox is None:
        print("panel has no ink -- threshold too high?")
        return
    print(f"panel             : {PANEL_W}x{PANEL_H}")
    print(f"ink bbox          : {bbox} ({bbox[2]-bbox[0]}x{bbox[3]-bbox[1]})")
    print(f"ink margins       : L={bbox[0]} R={PANEL_W-bbox[2]} "
          f"T={bbox[1]} B={PANEL_H-bbox[3]}")
    lit = sum(1 for p in panel.get_flattened_data() if p)
    print(f"lit pixels        : {lit} of {PANEL_W*PANEL_H} "
          f"({100*lit/(PANEL_W*PANEL_H):.1f}%)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="path to the 128x64 wordmark render")
    ap.add_argument("--check", action="store_true",
                    help="print the layout report only")
    args = ap.parse_args()

    source = Path(args.source) if args.source else DEFAULT_SOURCE
    if not source.is_file():
        raise SystemExit(f"source not found: {source}")
    print(f"source            : {source}")
    panel = load_panel(source)

    if args.check:
        report(panel)
        return

    OUT_HEADER.parent.mkdir(parents=True, exist_ok=True)
    header = to_c_header(panel)
    OUT_HEADER.write_text(header, encoding="utf-8")
    print(f"wrote {OUT_HEADER} ({len(header)} chars, "
          f"{len(panel.get_flattened_data())//8} bytes of bitmap)")

    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    panel.save(OUT_PNG)
    print(f"wrote {OUT_PNG} ({PANEL_W}x{PANEL_H}, true size)")

    print()
    report(panel)


if __name__ == "__main__":
    main()