# alcene-board-v1 Outline Refinement Report

- Source PCB: `X:\alcene\kicad\alcene-board-v1-layout-r3.kicad_pcb`
- Backup PCB: `X:\alcene\kicad\alcene-board-v1-before-outline-refinement.kicad_pcb`
- Refined PCB: `X:\alcene\kicad\alcene-board-v1-outline-refined.kicad_pcb`
- Date: 2026-10-20

## Result

- Original board dimensions: 160.00 mm x 130.00 mm.
- Final board dimensions: 111.354 mm x 84.381 mm.
- Left margin: 2.000 mm from silkscreen minimum X 35.736.
- Top margin: 2.000 mm from silkscreen minimum Y 33.685.
- Right margin: 2.000 mm from silkscreen maximum X 143.090.
- Bottom edge: 116.066 mm, set to the USB-C PCB Edge / mating-plane reference.

## USB-C alignment

- J2 is unchanged: X=41.525 mm, Y=109.966 mm, rotation=0°.
- Footprint: `Connector_USB:USB_C_Receptacle_GCT_USB4085`.
- Board bottom edge set to the footprint's PCB Edge reference at Y=116.066 mm.

## Non-Edge.Cuts object comparison

- Footprints: 14 before and after.
- Traces: 370 before and after.
- Zones: 1 before and after.
- Silkscreen texts: 40 before and after.
- Only `Edge.Cuts` was intentionally changed.

## DRC

- Total violations: 48
- Errors: 37
- Warnings: 11
- Clearance: 30
- Courtyards overlap: 3
- Copper edge clearance: 4
- Silk edge clearance: 2
- Via dangling: 1
- Silk overlap: 8

## Blocker

The compact bottom edge at the USB-C mating plane leaves the B.Cu GND zone fill only 0.166 mm from the board edge at the lower-right corner, below the 0.500 mm copper-edge clearance. Satisfying that clearance would require moving the bottom edge down by about 0.334 mm, which would move it away from the USB-C mating-plane reference. No non-`Edge.Cuts` object was changed to resolve this. The USB-C alignment was preserved and the conflict is reported.