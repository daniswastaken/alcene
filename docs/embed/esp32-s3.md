# ESP32-S3 platform notes

Target board: **ESP32-S3-DevKitC-1, N16R8** — 16 MB quad-SPI flash, 8 MB
octal (OPI) PSRAM. Framework: Arduino (ESP32 core 2.0.17).

## Build

```sh
pio run                  # compile
pio run -t upload        # flash
pio device monitor       # serial, 115200
```

Flash and monitor share one port: `Serial` stays on UART0, so whatever adapter
you flash through (FT232R, CH340, CP210x) is also where the boot report
appears. If you would rather use the S3's native USB connector instead, add
`-D ARDUINO_USB_CDC_ON_BOOT=1` to `build_flags` — but then the UART adapter
goes silent, which reads exactly like a dead board.

## Why `core_dir` is set

`platformio.ini` points `core_dir` at `C:\pioc`, a directory junction to
`%USERPROFILE%\.platformio`. This is not cosmetic.

The ESP32 Arduino core passes roughly 200 `-I` flags for the SDK, and every one
of them carries the full package path. On a deep Windows profile path those
flags total ~31 KB of the ~32 KB `CreateProcess` command-line limit, and the
build fails with a message that points nowhere useful:

```
xtensa-esp32s3-elf-g++.exe: error: CreateProcess: No such file or directory
```

That reads like a missing compiler. It is not — the toolchain compiles fine when
invoked directly. The `argv` simply does not fit. Measured on this machine, the
same command fails at 32,373 characters and succeeds at 32,139.

To recreate the junction after a reinstall of PlatformIO:

```sh
mklink /J C:\pioc "%USERPROFILE%\.platformio"
```

Drop the `core_dir` line if PlatformIO's home already lives somewhere short
(`C:\pio`, a short username, or a non-Windows host).

## PSRAM

N16R8 has **octal** PSRAM, so `board_build.arduino.memory_type` is `qio_opi`.
At the board default (`qio_qspi`) PSRAM does not map and `psramFound()` returns
false. `src/main.cpp` reports this on the OLED status screen and over serial, so
a misconfigured build is visible instead of silently degrading.

## OLED wiring

SSD1306 128x64 over I2C at address `0x3C`.

| Signal | Pin   | Notes                          |
| ------ | ----- | ------------------------------ |
| VCC    | 3V3   | 3.3 V only, never 5 V          |
| GND    | GND   |                                |
| SCL    | GPIO9 | I2C clock, 400 kHz             |
| SDA    | GPIO8 | I2C data                       |
| RES    | GPIO10| active low, 7-pin modules only |
| DC     | GPIO11| 7-pin modules only             |
| CS     | GPIO12| 7-pin modules only             |

Four-pin modules tie RES/DC/CS on the module and need only SDA, SCL, VCC, GND.
`Adafruit_SSD1306` is constructed with a reset pin of `-1`, which works for both
because the SSD1306's charge-pump start-up sequence is sufficient.

## The wordmark

`src/alcene_wordmark.h` is **generated** — edit the SVG, never the header.

- Editable master: `docs/static/wordmark.svg` (128x64, black background,
  white paths, custom `c` mark).
- Firmware source of truth: `docs/static/wordmark_128x64.png`, an exact
  128x64 raster of that SVG.

```sh
python tools/gen_wordmark.py          # regenerate header + preview
python tools/gen_wordmark.py --check  # layout report only
```

The generator converts pixels and nothing more: no crop, no re-centre, no
rescale. Layout, spacing and margins live in the SVG, where they belong.
Threshold is 128; the raster is nearly pure black/white with only a thin
anti-aliased fringe, so the cut point is not load-bearing.

To re-render the PNG after editing the SVG, rasterise it to exactly 128x64
with a black background (Edge headless at `--window-size=128,64` works; any
exact rasteriser works). Never rescale inside the generator.

Requires Python with Pillow.