# alcene-board-v1 Final Connectivity Report

## Net-level result

- Nets in PCB: 43 named/unnamed net entries including no-connect pads.
- Required nets routed: all schematic nets except intentional no-connect USB-C D+/D-/SBU pads.
- DRC unconnected items: 0.
- Copper zones refilled: yes, 1 GND zone on B.Cu.

## Critical net physical connectivity

| Net | Expected pads | Physical connection | Result |
|---|---:|---|---|
| GND | 26 | Tracks plus B.Cu zone | PASS |
| 3V3 | 12 | Tracks | PASS |
| VIN | 15 | Tracks and vias | PASS |
| Net-(J2-PadA5) | 2 | Tracks and via | PASS |
| Net-(J2-PadB5) | 2 | Tracks and via | PASS |
| RST | 2 | Track | PASS |
| GPIO0 through GPIO48 as assigned | 2-4 | Tracks | PASS |

## Topology notes

- Direct VBUS to VIN architecture preserved; no series diode or regulator added.
- CC1 and CC2 remain independent 5.1 kOhm sink pulldowns.
- J9 and J8 are distribution outputs only.
- J6 intentionally omits GPIO19; GPIO19 is routed only to J5 pin 1.
- C2 shifted 0.20 mm right; VIN and GND connectivity preserved.
- C1 pad 2 to C2 pad 1 clearance is 0.30 mm.
