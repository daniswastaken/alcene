# alcene-board-v1 Netlist Validation

## 1. Netlist source

- Fresh netlist generated with KiCad CLI 10.0.7:
  `X:\alcene\kicad\netlist-fresh.net`
- Source schematic:
  `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- Net count reported by schematic tool: 53 nets.

## 2. Critical power-net verification

### /VIN

Connections from fresh netlist:
- C1 pin 1
- C2 pin 1
- J1 pin 21
- J2 pins A4, A9, B4, B9
- J9 pins 1-8

Verification:
- J2 VBUS pins are all tied to VIN.
- C1 and C2 are on the VBUS/VIN side, upstream of where D1 was intended.
- J9 is a distribution header on VIN, not an independent source.
- D1 is absent, so there is no diode between J2 VBUS and VIN in the current schematic.

### /USB_VBUS relationship

The intended path was `J2 VBUS -> D1 -> /VIN`. The current schematic has `J2 VBUS -> /VIN` directly. The labels and wires do implement J2 VBUS to VIN, but not the documented reverse-blocking diode.

### /3V3

Connections from fresh netlist:
- J1 pins 1, 2
- J4 pins 1, 8
- J8 pins 1-8

Verification:
- /3V3 is the DevKit regulated 3.3 V rail.
- J8 is a distribution header on that rail.
- J4 VCC and backlight pin are on the same /3V3 net.

### /GND

Connections from fresh netlist:
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

Verification:
- USB-C receptacle shield is tied directly to GND.
- All distribution-header ground pins are tied to GND.
- Capacitor returns are tied to GND.

### /RST

Connections:
- SW1 pin 2
- J1 pin 3

Verification:
- SW1 pin 1 is GND.
- Reset switch is normally open momentary by component value and symbol.

## 3. USB-C CC1 and CC2

- J2 A5 (CC1) -> R1 pin 1 -> R1 pin 2 -> GND.
- J2 B5 (CC2) -> R2 pin 1 -> R2 pin 2 -> GND.
- CC1 and CC2 remain separate nets.
- Neither CC pin is tied to VBUS or directly to GND.
- Both resistors are 5.1 kohm.

## 4. GPIO breakout headers

J5 pin mapping verified from netlist:
1. GPIO19 from J3 pin 20
2. GPIO4 from J1 pin 4
3. GPIO5 from J1 pin 5
4. GPIO6 from J1 pin 6
5. GPIO7 from J1 pin 7
6. GPIO15 from J1 pin 8
7. GPIO16 from J1 pin 9
8. GPIO17 from J1 pin 10
9. GPIO18 from J1 pin 11
10. GPIO8 from J1 pin 12
11. GPIO3 from J1 pin 13
12. GPIO46 from J1 pin 14
13. GPIO9 from J1 pin 15
14. GPIO10 from J1 pin 16
15. GPIO11 from J1 pin 17
16. GPIO12 from J1 pin 18
17. GPIO13 from J1 pin 19
18. GPIO14 from J1 pin 20

J6 pin mapping verified from netlist:
1. TX from J3 pin 2
2. RX from J3 pin 3
3. GPIO1 from J3 pin 4
4. GPIO2 from J3 pin 5
5. GPIO42 from J3 pin 6
6. GPIO41 from J3 pin 7
7. GPIO40 from J3 pin 8
8. GPIO39 from J3 pin 9
9. GPIO38 from J3 pin 10
10. GPIO37 from J3 pin 11
11. GPIO36 from J3 pin 12
12. GPIO35 from J3 pin 13
13. GPIO0 from J3 pin 14
14. GPIO45 from J3 pin 15
15. GPIO48 from J3 pin 16
16. GPIO47 from J3 pin 17
17. GPIO21 from J3 pin 18
18. GPIO20 from J3 pin 19

Verification:
- J5 pin 1 is GPIO19 sourced from J3 pin 20.
- J6 intentionally omits GPIO19.
- No two GPIO nets are shorted in the netlist.
- No supply pin is exposed as a GPIO.

## 5. Power distribution headers

Verified:
- J7 pins 1-8 = GND.
- J8 pins 1-8 = 3V3.
- J9 pins 1-8 = VIN.

## 6. TFT pin-by-pin mapping

| J4 pin | Connected net | Expected function | Verification |
|---|---|---|---|
| 1 | 3V3 | Module VCC | Verified |
| 2 | GND | Module ground | Verified |
| 3 | GPIO10 | LCD_CS | Verified |
| 4 | GPIO8 | LCD_RST | Verified |
| 5 | GPIO9 | LCD_DC | Verified |
| 6 | GPIO11 | LCD_MOSI | Verified |
| 7 | GPIO12 | LCD_CLK | Verified |
| 8 | 3V3 | LCD_BL / LED | Verified electrically; current limiting unresolved |
| 9 | GPIO13 | LCD_MISO | Verified |
| 10 | GPIO12 | Touch CLK | Verified |
| 11 | GPIO14 | Touch CS | Verified |
| 12 | GPIO11 | Touch DIN | Verified |
| 13 | GPIO13 | Touch DOUT | Verified |
| 14 | GPIO15 | Touch IRQ | Verified |

## 7. Multiple-net-name warnings

ERC reported nine `multiple_net_names` warnings. These are aliases on the same net, not shorts:
- GPIO10 / LCD_CS
- GPIO8 / LCD_RST
- GPIO9 / LCD_DC
- GPIO12 / LCD_CLK
- 3V3 / LCD_BL
- GPIO14 / TOUCH_CS
- GPIO11 / TOUCH_DIN
- GPIO13 / TOUCH_DOUT
- GPIO15 / TOUCH_IRQ

Final netlist uses the GPIO or 3V3 name in each case. The aliases should be cleaned for documentation quality, but they do not change connectivity.

## 8. Unexpected or unresolved items

- D1 is absent, so USB VBUS is connected directly to VIN.
- J4 pin 8 backlight is tied directly to 3V3.
- C1/C2 electrical specifications are not recorded.
- Two wires cross the J1 symbol body (cosmetic).