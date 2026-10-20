# alcene-board-v1 Netlist Validation — Final Revision

- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- Fresh netlist: `X:\alcene\kicad\netlist-fresh.net`
- KiCad version: 10.0.7
- Date: 2026-10-20

## 1. /VIN

Connections:
- J2 pins A4, A9, B4, B9
- C1 pin 1
- C2 pin 1
- J1 pin 21
- J9 pins 1-8

Verification:
- J2 VBUS is directly connected to VIN.
- D1 is intentionally absent from this revision.
- C1 and C2 are on VIN and GND.
- J9 distributes VIN.

## 2. /3V3

Connections:
- J1 pins 1, 2
- J4 pins 1, 8
- J8 pins 1-8

## 3. /GND

Connections:
- J1 pin 22
- J2 pins A1, A12, B1, B12, SH
- J3 pins 1, 21, 22
- J4 pin 2
- J7 pins 1-8
- C1 pin 2
- C2 pin 2
- R1 pin 2
- R2 pin 2
- SW1 pin 1

## 4. /RST

Connections:
- J1 pin 3
- SW1 pin 2
- SW1 pin 1 -> GND

## 5. CC1 and CC2

- J2 A5 (CC1) -> R1 pin 1 -> R1 pin 2 -> GND.
- J2 B5 (CC2) -> R2 pin 1 -> R2 pin 2 -> GND.
- CC1 and CC2 are separate nets.

## 6. J5 and J6

J5:
1 GPIO19 from J3 pin 20
2 GPIO4 from J1 pin 4
3 GPIO5 from J1 pin 5
4 GPIO6 from J1 pin 6
5 GPIO7 from J1 pin 7
6 GPIO15 from J1 pin 8
7 GPIO16 from J1 pin 9
8 GPIO17 from J1 pin 10
9 GPIO18 from J1 pin 11
10 GPIO8 from J1 pin 12
11 GPIO3 from J1 pin 13
12 GPIO46 from J1 pin 14
13 GPIO9 from J1 pin 15
14 GPIO10 from J1 pin 16
15 GPIO11 from J1 pin 17
16 GPIO12 from J1 pin 18
17 GPIO13 from J1 pin 19
18 GPIO14 from J1 pin 20

J6:
1 TX from J3 pin 2
2 RX from J3 pin 3
3 GPIO1 from J3 pin 4
4 GPIO2 from J3 pin 5
5 GPIO42 from J3 pin 6
6 GPIO41 from J3 pin 7
7 GPIO40 from J3 pin 8
8 GPIO39 from J3 pin 9
9 GPIO38 from J3 pin 10
10 GPIO37 from J3 pin 11
11 GPIO36 from J3 pin 12
12 GPIO35 from J3 pin 13
13 GPIO0 from J3 pin 14
14 GPIO45 from J3 pin 15
15 GPIO48 from J3 pin 16
16 GPIO47 from J3 pin 17
17 GPIO21 from J3 pin 18
18 GPIO20 from J3 pin 19

Verification:
- J5 pin 1 carries GPIO19 from J3 pin 20.
- J6 intentionally omits GPIO19.
- No supply pin is exposed as a GPIO.

## 7. Power distribution headers

- J7 pins 1-8 -> GND.
- J8 pins 1-8 -> 3V3.
- J9 pins 1-8 -> VIN.

## 8. TFT connector

| J4 pin | Net | Function |
|---|---|---|
| 1 | 3V3 | VCC |
| 2 | GND | GND |
| 3 | GPIO10 | LCD_CS |
| 4 | GPIO8 | LCD_RST |
| 5 | GPIO9 | LCD_DC |
| 6 | GPIO11 | LCD_MOSI |
| 7 | GPIO12 | LCD_CLK |
| 8 | 3V3 | LCD_BL direct, owner-confirmed |
| 9 | GPIO13 | LCD_MISO |
| 10 | GPIO12 | TOUCH_CLK |
| 11 | GPIO14 | TOUCH_CS |
| 12 | GPIO11 | TOUCH_DIN |
| 13 | GPIO13 | TOUCH_DOUT |
| 14 | GPIO15 | TOUCH_IRQ |

## 9. Label cleanup result

Redundant electrical alias labels were removed. Electrical connectivity is unchanged. The final netlist resolves the shared TFT nets to GPIO names or 3V3. No VCC, LCD_*, or TOUCH_* electrical alias labels remain on those nets. TFT functions are documented with non-electrical text.