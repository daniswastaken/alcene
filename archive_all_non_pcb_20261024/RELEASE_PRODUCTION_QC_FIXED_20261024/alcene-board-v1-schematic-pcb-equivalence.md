# Schematic-to-PCB Equivalence

Fresh netlist generated from X:\alcene\kicad\alcene-board-v1.kicad_sch.
Final PCB: X:\alcene\kicad\ALCENE_PRODUCTION_QC_FIXED_20261024.kicad_pcb.

J4 pad mapping verified against schematic:
1 3V3, 2 GND, 3 GPIO10, 4 GPIO8, 5 GPIO9, 6 GPIO11, 7 GPIO12, 8 3V3, 9 GPIO13, 10 GPIO12, 11 GPIO14, 12 GPIO11, 13 GPIO13, 14 GPIO15.

Shared GPIO branches preserved: GPIO11 pads 6/12, GPIO12 pads 7/10, GPIO13 pads 9/13.
Power, CC, reset, and GPIO breakout mappings match the schematic. ERC passes with 0 violations.