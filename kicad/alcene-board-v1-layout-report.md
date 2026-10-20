# alcene-board-v1 PCB Layout Report

- PCB: `X:\alcene\kicad\alcene-board-v1-layout-r2.kicad_pcb`
- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- KiCad version: 10.0.7
- Date: 2026-10-20
- Layers: F.Cu and B.Cu only

## Placement summary

- Board outline: 120 mm x 90 mm rectangle.
- J5 and J6 placed as a tightly paired 2-column x 18-row GPIO breakout block at the left.
- J1 and J3 placed immediately to the right of the GPIO block.
- J8, J7, and J9 placed along the top edge, left to right.
- Each power header rotated to a horizontal 4-column x 2-row assembly.
- SW1 placed left of J2 near the bottom-left.
- J4 placed horizontally along the bottom edge of the TFT reservation.
- TFT reservation and `2.8 INCH TFT DISPLAY AREA` label placed on F.Silkscreen on the right side.
- GPIO labels placed on the outer left and right sides of J5 and J6.

## Routing summary

- Autorouter: Freerouting, 1 attempt, 50 passes, 21.0 s.
- Tracks: 342.
- Vias: 8.
- Ground copper pour added on B.Cu for GND.
- All schematic nets were imported; six USB-C data/SBU pads are intentionally unconnected.

## DRC result

- Total violations: 66
- Errors: 33
- Warnings: 33
- Clearance: 30
- Courtyards overlap: 3
- Silkscreen overlap: 33
- Track width: 0 after widening 44 narrow traces to 0.2 mm

## Remaining issues

- Clearance violations remain around the USB-C footprint and dense routing.
- Courtyard overlaps occur between closely spaced passives and between the intentionally tight J5/J6 pair.
- Silkscreen overlaps occur where GPIO labels are close to component bodies and pads.
- Mechanical fit of the DevKit and TFT module was not independently verified beyond the schematic footprint data.

## Status

Layout and autorouting are complete, but the board is not yet DRC-clean. It is not approved for prototype fabrication until clearance, courtyard, and silkscreen violations are resolved or explicitly accepted. No PCB layout reuse from prior revisions was performed. No schematic electrical changes were made.