# Connectivity Report - ALCENE_TFT_ROUTING_VERIFIED_RELEASE_20261024

Source PCB: X:\alcene\kicad\alcene-board-v1-forensic-routing-fixed.kicad_pcb
Final PCB: X:\alcene\kicad\ALCENE_TFT_ROUTING_VERIFIED_RELEASE_20261024.kicad_pcb
Schematic: X:\alcene\kicad\alcene-board-v1.kicad_sch

## J4 pinout verification
J4 pads 1-14 are physically left-to-right and match the required mapping:
1 3V3, 2 GND, 3 GPIO10, 4 GPIO8, 5 GPIO9, 6 GPIO11, 7 GPIO12, 8 3V3, 9 GPIO13, 10 GPIO12, 11 GPIO14, 12 GPIO11, 13 GPIO13, 14 GPIO15.

## Routed nets
J4 power/ground: 3V3 pads 1/8 connected to J1/J8 network; GND pad 2 connected to GND network.
LCD signals: GPIO10, GPIO8, GPIO9, GPIO11, GPIO12, GPIO13 routed to J1 and J5 branches.
Touch signals: GPIO12, GPIO14, GPIO11, GPIO13, GPIO15 routed to J1 and J5 branches.
Shared GPIO branches preserved: GPIO11 (pads 6/12), GPIO12 (pads 7/10), GPIO13 (pads 9/13).

## Power architecture
VIN connects J2 VBUS contacts, C1/C2, J1 pin 21, J9 pads 1-8. CC1/CC2 remain separate through R1/R2. Reset connects J1 pin 3 to SW1 pad 2.

## DRC summary
Errors: 49, Warnings: 6. Full report: ALCENE_TFT_ROUTING_VERIFIED_RELEASE_20261024_drc.txt. Remaining violations are documented pre-existing clearance/courtyard/silk exceptions plus routing crossings introduced by RST detour. No unconnected items remain except two documented GND pad-to-copper items.