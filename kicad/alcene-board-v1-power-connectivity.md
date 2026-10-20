# alcene-board-v1 Power Connectivity

- PCB: `X:\alcene\kicad\alcene-board-v1-connectivity-verified.kicad_pcb`
- Date: 2026-10-20

## VIN

J2/A4, A9, B4, B9; C1/1; C2/1; J1/21; J9/1-8 are assigned to VIN and form one connected network. Direct VBUS-to-VIN architecture is preserved. No D1 is present.

## 3V3

J1/1, J1/2; J4/1, J4/8; J8/1-8 are assigned to 3V3 and form one connected network.

## CC1 and CC2

- CC1: J2/A5 to R1/1; R1/2 to GND.
- CC2: J2/B5 to R2/1; R2/2 to GND.
- CC1 and CC2 remain separate.

## Reset

- J1/3 to SW1/2.
- SW1/1 to GND.

## GPIO and TFT

All GPIO breakout and TFT connector pads were checked against the schematic netlist. Their pad-to-net assignments match the approved schematic, including GPIO19 on J5 pin 1, no GPIO19 on J6, and the direct 3V3 backlight connection on J4 pin 8. DRC reports no unconnected items.