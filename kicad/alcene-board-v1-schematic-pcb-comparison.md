# alcene-board-v1 Schematic-to-PCB Comparison

## Summary

- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- PCB: `X:\alcene\kicad\alcene-board-v1-final-qc.kicad_pcb`
- ERC: 0 errors, 0 warnings, 0 info
- Component correspondence: PASS
- Pad-to-net comparison: PASS
- Physical copper connectivity: PASS for all required nets; DRC reports no unconnected items

## Component correspondence

| Reference | Schematic symbol/value | PCB footprint | Pad mapping | Net consistency | Result |
|---|---|---|---|---|---|
| J1 | Connector:Conn_01x22_Socket / ESP32-S3-DevKitC-1_J1 | Connector_PinSocket_2.54mm:PinSocket_1x22_P2.54mm_Vertical | 22/22 | PASS | PASS |
| J2 | Connector:USB_C_Receptacle_USB2.0_16P / USB-C Input | Connector_USB:USB_C_Receptacle_GCT_USB4085 | 20/20 | PASS | PASS |
| J3 | Connector:Conn_01x22_Socket / ESP32-S3-DevKitC-1_J3 | Connector_PinSocket_2.54mm:PinSocket_1x22_P2.54mm_Vertical | 22/22 | PASS | PASS |
| J4 | Connector:Conn_01x14_Socket / ILI9341_TFT_14pin | Connector_PinSocket_2.54mm:PinSocket_1x14_P2.54mm_Vertical | 14/14 | PASS | PASS |
| J5 | Connector:Conn_01x18_Pin / Male Pin Header 1x18 - J1 Signals | Connector_PinHeader_2.54mm:PinHeader_1x18_P2.54mm_Vertical | 18/18 | PASS | PASS |
| J6 | Connector:Conn_01x18_Pin / Male Pin Header 1x18 - J3 Signals | Connector_PinHeader_2.54mm:PinHeader_1x18_P2.54mm_Vertical | 18/18 | PASS | PASS |
| J7 | Connector_Generic:Conn_02x04_Odd_Even / Male Pin Header 2x4 - GND | Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical | 8/8 | PASS | PASS |
| J8 | Connector_Generic:Conn_02x04_Odd_Even / Male Pin Header 2x4 - 3V3 | Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical | 8/8 | PASS | PASS |
| J9 | Connector_Generic:Conn_02x04_Odd_Even / Male Pin Header 2x4 - VIN 5V | Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical | 8/8 | PASS | PASS |
| R1 | Device:R / 5.1k | Resistor_SMD:R_0805_2012Metric | 2/2 | PASS | PASS |
| R2 | Device:R / 5.1k | Resistor_SMD:R_0805_2012Metric | 2/2 | PASS | PASS |
| C1 | Device:C / 10uF | Capacitor_SMD:C_0805_2012Metric | 2/2 | PASS | PASS |
| C2 | Device:C / 100nF | Capacitor_SMD:C_0805_2012Metric | 2/2 | PASS | PASS |
| SW1 | Switch:SW_Push / ESP32-S3 Reset (NO momentary) | Button_Switch_SMD:SW_Push_SPST_NO_Alps_SKRK | 2/2 | PASS | PASS |

## Power and critical nets

- GND: 26 pads, physical connection verified by copper and B.Cu GND zone.
- 3V3: 12 pads, physical connection verified.
- VIN: 15 pads plus J9 distribution outputs, physical connection verified.
- CC1: J2 A5 -> R1 pin 1 -> R1 pin 2 -> GND.
- CC2: J2 B5 -> R2 pin 1 -> R2 pin 2 -> GND.
- RST: J1 pin 3 -> SW1 pin 2; SW1 pin 1 -> GND.

## TFT mapping verified

J4 pins 1-14: 3V3, GND, GPIO10, GPIO8, GPIO9, GPIO11, GPIO12, 3V3, GPIO13, GPIO12, GPIO14, GPIO11, GPIO13, GPIO15. All match schematic.

## Notes

- Mounting holes MH1 and MH2 exist only on the PCB and are not schematic components.
- USB-C D+, D-, and SBU pads are intentionally unconnected per schematic no-connects.
- No schematic changes were made.
