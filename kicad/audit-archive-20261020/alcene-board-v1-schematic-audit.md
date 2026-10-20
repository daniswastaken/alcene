# alcene-board-v1 Schematic Audit

## 1. Project and files

- Authoritative schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- KiCad version: 10.0.7 (`kicad-cli.exe`)
- Audit date: 2026-10-20
- Original backup created before audit: `X:\alcene\kicad\alcene-board-v1.kicad_sch.audit-backup-2026-10-20`
- Fresh ERC report: `X:\alcene\kicad\erc-fresh.json`
- Fresh netlist: `X:\alcene\kicad\netlist-fresh.net`

No schematic modification was made during the initial audit.

## 2. Component inventory

15 schematic symbols:

| Ref | Library:Symbol | Value | Footprint |
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

Important finding: no D1 symbol exists in the current schematic. The design intent and backup schematic both include D1 = `Device:D_Schottky`, value `SS14 (onsemi, 40V 1A Schottky)`, footprint `Diode_SMD:D_SMA`, with manufacturer `onsemi`, MPN `SS14`.

## 3. Structural findings

- Schematic file validates structurally (`validate_schematic`, 0 errors, 0 warnings).
- Grid check: no off-grid geometry.
- No orphaned wires.
- No floating net labels.
- No overlapping elements.
- ERC: 0 errors, 9 warnings. All warnings are `multiple_net_names`.
- Two wires cross the J1 symbol body. This is a cosmetic/routing-quality issue, not an electrical error:
  - `(129.54,104.14) -> (116.84,104.14)` crosses J1.
  - `(142.24,55.88) -> (116.84,55.88)` crosses J1.
- Six no-connect markers are present on J2 D+/D-/SBU pins. This is consistent with a USB-C power-only input.

## 4. Symbol, footprint, and property audit

### J2 USB-C

- Symbol: `Connector:USB_C_Receptacle_USB2.0_16P`, 17 pins.
- Footprint: `Connector_USB:USB_C_Receptacle_GCT_USB4085`.
- VBUS pins A4, A9, B4, B9 are tied together.
- CC1 (A5) and CC2 (B5) are separate.
- Shield pin SH is tied to GND.
- USB data/SBU pins are no-connected.

### J1 / J3 DevKit sockets

- 22 pins each, 2.54 mm pitch.
- Footprint: `PinSocket_1x22_P2.54mm_Vertical`.
- Pin mapping matches the official ESP32-S3-DevKitC-1 v1.1 header table for J1 and J3 (see netlist validation report).

### J4 TFT connector

- 14 pins, 2.54 mm pitch.
- Footprint: `PinSocket_1x14_P2.54mm_Vertical`.
- VCC and backlight-related pin 8 are tied to the 3V3 net through multiple labels.

### Power distribution headers

- J7, J8, J9: `Conn_02x04_Odd_Even`, footprint `PinHeader_2x04_P2.54mm_Vertical`.
- All pins of each header are tied to one net (GND, 3V3, VIN respectively).

### Passives

- R1 and R2: 5.1 kohm, 0805 footprint.
- C1: 10 uF, 0805 footprint.
- C2: 100 nF, 0805 footprint.
- No voltage rating, dielectric, or tolerance is recorded for C1/C2. This is an unresolved specification gap.

### Power flag

- `#FLG01` is attached to the VIN/USB_VBUS side through C1/C2 pin 1.
- It is a KiCad ERC power source marker, not proof of a safe or regulated physical supply.

## 5. TFT compatibility findings

- J4 pin mapping matches the common ILI9341 14-pin module order:
  - Pin 1 VCC -> 3V3
  - Pin 2 GND
  - Pin 3 CS -> GPIO10
  - Pin 4 RESET -> GPIO8
  - Pin 5 DC -> GPIO9
  - Pin 6 MOSI -> GPIO11
  - Pin 7 CLK -> GPIO12
  - Pin 8 LED/backlight -> 3V3 (merged with VCC)
  - Pin 9 MISO -> GPIO13
  - Pin 10 touch CLK -> GPIO12
  - Pin 11 touch CS -> GPIO14
  - Pin 12 touch DIN -> GPIO11
  - Pin 13 touch DOUT -> GPIO13
  - Pin 14 touch IRQ -> GPIO15
- The exact TFT module and its onboard backlight current limiting are not established by the schematic or project files.
- Backlight pin 8 is tied directly to 3V3 with no series resistor in the schematic.

## 6. ESP32-S3 compatibility findings

- J1/J3 pin numbers and GPIO assignments match the official ESP32-S3-DevKitC-1 v1.1 table.
- GPIO19 and GPIO20 are exposed on J5/J6 and are also the DevKit's USB D-/D+ signals. Using them as general GPIO conflicts with native USB.
- GPIO0 is exposed on J6 pin 13 and is a boot strapping pin.
- GPIO45 and GPIO46 are exposed; GPIO46 is input-only on the ESP32-S3.
- GPIO35, GPIO36, and GPIO37 are exposed. On Octal SPI flash/PSRAM DevKit variants these pins are used internally and are not available externally.
- The DevKit's power options are mutually exclusive: USB, 5V/GND, or 3V3/GND. The schematic drives J1 pin 21 (5V) from VIN and also exposes J1 pins 1-2 as 3V3.

## 7. Unresolved assumptions

- Exact TFT module part number and backlight circuit.
- C1/C2 voltage rating and dielectric.
- Actual USB source current capability.
- Physical connector dimensions and mating clearances.
- Whether the intended D1 removal was deliberate or accidental. The current schematic does not implement the documented D1.