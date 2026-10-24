# alcene-board-v1 Production QC Report

Source PCB: X:\alcene\kicad\alcene-board-v1-forensic-routing-fixed.kicad_pcb
Backup: X:\alcene\kicad\ALCENE_PRODUCTION_QC_SOURCE_BACKUP_20261024.kicad_pcb
Final PCB: X:\alcene\kicad\ALCENE_PRODUCTION_QC_FIXED_20261024.kicad_pcb
Schematic: X:\alcene\kicad\alcene-board-v1.kicad_sch
Release: X:\alcene\kicad\RELEASE_PRODUCTION_QC_FIXED_20261024

Initial DRC: 49 violations (clearance, hole_clearance, courtyard, solder_mask_bridge, silk).
Final DRC: 38 violations (29 clearance, 3 courtyard_overlap, 6 silk_overlap). No shorts, no crossings, no unconnected items, no dangling tracks.
ERC: 0 errors, 0 warnings.
Unrouted count: 0 required unconnected items in final DRC.

Repairs: removed obsolete J4 diagonal tracks, reconstructed J4-to-ESP32 routing with autorouter, removed dangling RST fragments, replaced 0.15 mm tracks with 0.2 mm, preserved GND zone and refilled.

J4 pads 1-14 verified left-to-right with required net mapping and shared GPIO branches preserved.
Power architecture preserved: USB-C VBUS to VIN, J1 pin 21 and J9 pads 1-8 on VIN, C1/C2 VIN-GND, 3V3 and GND distribution.
J9 silkscreen has exactly one visible 5V label; no VIN text.
Board uses only F.Cu and B.Cu. Component placement and outline preserved.