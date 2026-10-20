# alcene-board-v1 Schematic Audit — Final Revision

- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- KiCad version: 10.0.7
- Audit/correction date: 2026-10-20
- Previous report archive: `X:\alcene\kicad\audit-archive-20261020`
- Original schematic backup: `X:\alcene\kicad\alcene-board-v1.kicad_sch.audit-backup-2026-10-20`
- Fresh ERC: `X:\alcene\kicad\erc-fresh.json`
- Fresh netlist: `X:\alcene\kicad\netlist-fresh.net`

## 1. Final architecture

- Power path is intentionally direct: `J2 USB-C VBUS -> VIN -> J1 pin 21 and J9 pins 1-8`.
- D1 is intentionally absent from this revision. No reverse-current blocking is provided between J2 VBUS and VIN.
- J8 and J9 are distribution outputs only. They must not be used as external power inputs.
- J2 USB power and DevKit native USB power must not be used simultaneously.
- DevKit power inputs remain mutually exclusive.
- TFT pinout and direct 3V3 backlight connection are owner-confirmed and were preserved.

## 2. Component inventory

15 placed symbols. No D1. J2 VBUS is directly tied to VIN. C1 and C2 are on VIN and GND.

| Ref | Symbol | Value | Footprint |
|---|---|---|---|
| J1 | Connector:Conn_01x22_Socket | ESP32-S3-DevKitC-1_J1 | Connector_PinSocket_2.54mm:PinSocket_1x22_P2.54mm_Vertical |
| J3 | Connector:Conn_01x22_Socket | ESP32-S3-DevKitC-1_J3 | Connector_PinSocket_2.54mm:PinSocket_1x22_P2.54mm_Vertical |
| J2 | Connector:USB_C_Receptacle_USB2.0_16P | USB-C Input | Connector_USB:USB_C_Receptacle_GCT_USB4085 |
| J4 | Connector:Conn_01x14_Socket | ILI9341_TFT_14pin | Connector_PinSocket_2.54mm:PinSocket_1x14_P2.54mm_Vertical |
| J5 | Connector:Conn_01x18_Pin | Male Pin Header 1x18 - J1 Signals | Connector_PinHeader_2.54mm:PinHeader_1x18_P2.54mm_Vertical |
| J6 | Connector:Conn_01x18_Pin | Male Pin Header 1x18 - J3 Signals | Connector_PinHeader_2.54mm:PinHeader_1x18_P2.54mm_Vertical |
| J7 | Connector_Generic:Conn_02x04_Odd_Even | Male Pin Header 2x4 - GND | Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical |
| J8 | Connector_Generic:Conn_02x04_Odd_Even | Male Pin Header 2x4 - 3V3 | Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical |
| J9 | Connector_Generic:Conn_02x04_Odd_Even | Male Pin Header 2x4 - VIN 5V | Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical |
| SW1 | Switch:SW_Push | ESP32-S3 Reset (NO momentary) | Button_Switch_SMD:SW_Push_SPST_NO_Alps_SKRK |
| R1 | Device:R | 5.1k | Resistor_SMD:R_0805_2012Metric |
| R2 | Device:R | 5.1k | Resistor_SMD:R_0805_2012Metric |
| C1 | Device:C | 10uF | Capacitor_SMD:C_0805_2012Metric |
| C2 | Device:C | 100nF | Capacitor_SMD:C_0805_2012Metric |
| #FLG01 | power:PWR_FLAG | PWR_FLAG | none |

## 3. Final capacitor specifications

- C1: Murata `GRM21BZ71E106KE15L`, 10 uF, 25 V, X7R, +/-10%, 0805.
- C2: Murata `GRM21BR71H104KA01L`, 100 nF, 50 V, X7R, +/-10%, 0805.
- C1 DC-bias derating must be checked in the Murata datasheet/SimSurfing tool; its effective capacitance at 5 V may be below the nominal 10 uF.
- C2 is suitable for high-frequency decoupling on a 5 V rail.

## 4. Structural and electrical validation

- Schematic validates structurally: 0 errors, 0 warnings.
- No orphaned wires.
- No floating labels.
- No wires crossing symbols after cleanup.
- ERC: 0 errors, 0 warnings (`erc-fresh.json`).
- Net count after cleanup: 40.

## 5. USB-C input

- J2 VBUS pins A4, A9, B4, B9 are tied to VIN.
- CC1 (A5) -> R1 -> GND.
- CC2 (B5) -> R2 -> GND.
- CC1 and CC2 remain separate.
- Shield pin SH is tied to GND.
- D+/D-/SBU pins have no-connect markers.
- Two 5.1 kohm CC pull-downs implement a basic USB Type-C sink. This does not by itself detect or negotiate 1.5 A or 3 A source capability.

## 6. ESP32-S3 compatibility

- J1/J3 pin mapping matches the official ESP32-S3-DevKitC-1 v1.1 header table.
- GPIO19 and GPIO20 are exposed and are also DevKit USB D-/D+ signals.
- GPIO0 is exposed and is a boot strapping pin.
- GPIO46 is input-only.
- GPIO35-37 may be unavailable on Octal SPI flash/PSRAM variants.
- J1 pin 21 receives VIN. J1 pins 1-2 provide 3V3.

## 7. TFT interface

Owner-confirmed and preserved:
- J4 pin 1 -> 3V3
- J4 pin 2 -> GND
- J4 pin 3 -> GPIO10 (LCD_CS)
- J4 pin 4 -> GPIO8 (LCD_RST)
- J4 pin 5 -> GPIO9 (LCD_DC)
- J4 pin 6 -> GPIO11 (LCD_MOSI)
- J4 pin 7 -> GPIO12 (LCD_CLK)
- J4 pin 8 -> 3V3 (LCD_BL, direct, owner-confirmed)
- J4 pin 9 -> GPIO13 (LCD_MISO)
- J4 pin 10 -> GPIO12 (TOUCH_CLK)
- J4 pin 11 -> GPIO14 (TOUCH_CS)
- J4 pin 12 -> GPIO11 (TOUCH_DIN)
- J4 pin 13 -> GPIO13 (TOUCH_DOUT)
- J4 pin 14 -> GPIO15 (TOUCH_IRQ)

Redundant electrical alias labels were removed. TFT functions are documented with non-electrical text near J4. Electrical net names remain GPIO-based or 3V3.

## 8. Power headers

- J7 pins 1-8 -> GND.
- J8 pins 1-8 -> 3V3.
- J9 pins 1-8 -> VIN.
- These are distribution outputs only, not alternative power inputs.

## 9. Schematic notes added

The schematic contains concise notes stating:
- J2 USB-C is the external power input.
- J8 3V3 and J9 VIN are distribution outputs only.
- Do not inject external power through these headers.
- Do not connect J2 USB power and DevKit native USB power simultaneously.
- DevKit power inputs are mutually exclusive.
- Direct VBUS-to-VIN connection; reverse-current blocking is not provided.

## 10. Remaining limitations

- No reverse-current blocking between J2 VBUS and VIN.
- USB source current capability is not detected beyond basic Type-C sink configuration.
- C1 effective capacitance under DC bias must be checked against the Murata datasheet.
- Physical connector fit and mechanical clearances remain unverified.
- TFT module exact part number and backlight electrical design are owner-confirmed but not independently datasheet-verified.