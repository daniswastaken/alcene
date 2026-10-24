# Real copper connectivity - alcene-board-v2 (rebase, zero-DRC)

Date: 2026-10-24

All numbers below are parsed from the shipped file
`alcene-board-v2-rebased-zero-drc.kicad_pcb` itself (not from in-memory
state).

## Headline

- Nets: **42** named nets (+ netcode-0 blank, see equivalence report).
- Copper: **329 segments** (F.Cu 212 / B.Cu 117), all `(width 0.2)` mm, **4 vias** (0.6/0.3).
- Zones: **0** - every net is real A-to-B track copper; no pours, no ratsnest-hiding.
- Final DRC: **0 DRC violations, 0 unconnected pads, 0 footprint errors**
  (footer of `alcene-board-v2-final-drc-report.txt`).

## Per-net table

| Net | Pads | Segments (F) | Segments (B) | Vias | Track length, mm |
|---|---|---|---|---|---|
| `3V3` | 12 | 38 | 16 | 22 | 0 | 137.92 |
| `GND` | 23 | 47 | 31 | 16 | 1 | 226.90 |
| `GPIO0` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO1` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO10` | 3 | 15 | 4 | 11 | 0 | 92.09 |
| `GPIO11` | 4 | 21 | 10 | 11 | 0 | 88.56 |
| `GPIO12` | 4 | 9 | 4 | 5 | 0 | 79.24 |
| `GPIO13` | 4 | 17 | 10 | 7 | 0 | 76.72 |
| `GPIO14` | 3 | 9 | 3 | 6 | 0 | 67.52 |
| `GPIO15` | 3 | 9 | 4 | 5 | 0 | 92.67 |
| `GPIO16` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO17` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO18` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO19` | 2 | 5 | 0 | 5 | 0 | 48.77 |
| `GPIO2` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO20` | 2 | 3 | 3 | 0 | 0 | 17.73 |
| `GPIO21` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO3` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO35` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO36` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO37` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO38` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO39` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO4` | 2 | 3 | 3 | 0 | 0 | 39.26 |
| `GPIO40` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO41` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO42` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO45` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO46` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO47` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO48` | 2 | 4 | 4 | 0 | 0 | 17.73 |
| `GPIO5` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO6` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO7` | 2 | 4 | 4 | 0 | 0 | 39.26 |
| `GPIO8` | 3 | 6 | 4 | 2 | 0 | 92.21 |
| `GPIO9` | 3 | 6 | 4 | 2 | 0 | 86.52 |
| `Net-(J2-PadA5)` | 2 | 7 | 1 | 6 | 1 | 15.08 |
| `Net-(J2-PadB5)` | 2 | 3 | 3 | 0 | 0 | 11.02 |
| `RST` | 2 | 3 | 1 | 2 | 1 | 63.05 |
| `RX` | 2 | 5 | 5 | 0 | 0 | 19.33 |
| `TX` | 2 | 3 | 0 | 3 | 0 | 17.73 |
| `VIN` | 15 | 28 | 14 | 14 | 1 | 183.40 |
## Vias

| Net | At (x, y) | Type |
|---|---|---|
| `GND` | 115.4262, 118.1738 | F.Cu<->B.Cu |
| `Net-(J2-PadA5)` | 51.5919, 114.6044 | F.Cu<->B.Cu |
| `RST` | 113.5913, 113.9913 | F.Cu<->B.Cu |
| `VIN` | 114.7811, 100.7293 | F.Cu<->B.Cu |
## Connector pad inventory

| Ref | Value | Net x count |
|---|---|---|
| `C1` | 10uF | GNDx1; VINx1 |
| `C2` | 100nF | GNDx1; VINx1 |
| `J1` | ESP32-S3-DevKitC-1_J1 | 3V3x2; GNDx1; GPIO10x1; GPIO11x1; GPIO12x1; GPIO13x1; GPIO14x1; GPIO15x1; GPIO16x1; GPIO17x1; GPIO18x1; GPIO3x1; GPIO4x1; GPIO46x1; GPIO5x1; GPIO6x1; GPIO7x1; GPIO8x1; GPIO9x1; RSTx1; VINx1 |
| `J2` | USB-C Input | GNDx8; Net-(J2-PadA5)x1; Net-(J2-PadB5)x1; VINx4 |
| `J3` | ESP32-S3-DevKitC-1_J3 | GNDx3; GPIO0x1; GPIO1x1; GPIO19x1; GPIO2x1; GPIO20x1; GPIO21x1; GPIO35x1; GPIO36x1; GPIO37x1; GPIO38x1; GPIO39x1; GPIO40x1; GPIO41x1; GPIO42x1; GPIO45x1; GPIO47x1; GPIO48x1; RXx1; TXx1 |
| `J4` | ILI9341_TFT_14pin | 3V3x2; GNDx1; GPIO10x1; GPIO11x2; GPIO12x2; GPIO13x2; GPIO14x1; GPIO15x1; GPIO8x1; GPIO9x1 |
| `J5` | Male Pin Header 1x18 - J1 Signals | GPIO10x1; GPIO11x1; GPIO12x1; GPIO13x1; GPIO14x1; GPIO15x1; GPIO16x1; GPIO17x1; GPIO18x1; GPIO19x1; GPIO3x1; GPIO4x1; GPIO46x1; GPIO5x1; GPIO6x1; GPIO7x1; GPIO8x1; GPIO9x1 |
| `J6` | Male Pin Header 1x18 - J3 Signals | GPIO0x1; GPIO1x1; GPIO2x1; GPIO20x1; GPIO21x1; GPIO35x1; GPIO36x1; GPIO37x1; GPIO38x1; GPIO39x1; GPIO40x1; GPIO41x1; GPIO42x1; GPIO45x1; GPIO47x1; GPIO48x1; RXx1; TXx1 |
| `J7` | Male Pin Header 2x4 - GND | GNDx8 |
| `J8` | Male Pin Header 2x4 - 3V3 | 3V3x8 |
| `J9` | Male Pin Header 2x4 - VIN 5V | VINx8 |
| `MH1` | MountingHole_3mm | (no nets - mounting) |
| `MH2` | MountingHole_3mm | (no nets - mounting) |
| `R1` | 5.1k | GNDx1; Net-(J2-PadA5)x1 |
| `R2` | 5.1k | GNDx1; Net-(J2-PadB5)x1 |
| `SW1` | ESP32-S3 Reset (NO momentary) | GNDx1; RSTx1 |
