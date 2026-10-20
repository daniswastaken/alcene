# alcene-board-v1 Connectivity Audit

- Source PCB: `X:\alcene\kicad\alcene-board-v1-connectivity-verified.kicad_pcb`
- Backup PCB: `X:\alcene\kicad\alcene-board-v1-before-connectivity-audit.kicad_pcb`
- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- KiCad version: 10.0.7
- Date: 2026-10-20

## Initial and final status

- Initial unrouted connections: 0
- Final unrouted connections: 0
- Initial DRC: 41 violations
- Final DRC: 41 violations
- Repairs made: 0 connectivity repairs
- Copper zones refilled: 1 GND zone

## Verification performed

- Fresh netlist generated from the approved schematic.
- PCB pad-to-net assignments compared against the netlist.
- GND, 3V3, VIN, RST, CC1, CC2, GPIO, and TFT nets checked.
- Actual DRC run after zone refill.

## Findings

No missing or incorrect schematic-to-PCB connectivity was found. All required nets are routed. The remaining DRC violations are clearance, courtyard-overlap, and silkscreen-overlap issues, not unrouted or unconnected nets.

## Component preservation

No footprint was moved, rotated, replaced, added, or deleted. The board outline and silkscreen were not changed. Only the GND copper zone was refilled.