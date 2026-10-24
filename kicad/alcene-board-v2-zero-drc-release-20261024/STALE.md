# STALE — do not use this release package

**Status: STALE** — flagged 2026-10-24.

This package (Gerbers, drill files, netlist, DRC/ERC reports, BOM, and report set
generated 2026-10-24 for `alcene-base.kicad_pcb` / the pre-refinement
`alcene-board-v2-rebased-zero-drc.kicad_pcb`) no longer reflects the shipped board.

## What superseded it

The board file `X:\alcene\kicad\alcene-board-v2-rebased-zero-drc.kicad_pcb` was
layout-refined after this package was exported. Changes that invalidate everything here:

- New board outline (123.0 x 92.8762 mm, was 123.0 x 90.0).
- New F.SilkS display reservation 50.0 x 85.0 mm centered on x = 77.26, with the
  alcene logo re-centered inside it.
- Mounting holes repositioned (spacing 45.19 mm preserved), references moved inside the board.
- Passives C1/C2/R1/R2 repositioned and rotated; silk field column added.
- J6 moved for a tight 2x18 breakout with J5 (pin pitch 2.54 mm across the two columns);
  J6's 18 nets re-routed, header silk rings removed.
- Island (J2/VIN/GND) routing changed.

The electrical design is unchanged (schematic `alcene-board-v1.kicad_sch` untouched;
netlist equivalence verified 42 nets / 139 nodes identical), but every geometry-derived
output in this package is out of date.

## Why you must not use this package

- Gerbers/drill: cut-out, silk, and hole positions no longer match the board.
- DRC/ERC reports in here predate the refinement.
- Netlist/BOM: position data invalid; connectivity report reflects the old routing.

## Authoritative state

- Board: `X:\alcene\kicad\alcene-board-v2-rebased-zero-drc.kicad_pcb`
  (fresh DRC: 0 violations / 0 unconnected; ERC: 0 violations).
- Refinement details and measured values:
  `X:\alcene\kicad\alcene-board-v2-layout-refinement-report.md`.

Re-export manufacturing data from the current board file if fabrication output is needed.
