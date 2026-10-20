# alcene-board-v1 DRC Report

- PCB: `X:\alcene\kicad\alcene-board-v1-layout-r2.kicad_pcb`
- Date: 2026-10-20
- KiCad version: 10.0.7
- Report source: `X:\alcene\kicad\alcene-board-v1-layout-r2_drc_violations.json`

## Summary

- Total violations: 66
- Errors: 33
- Warnings: 33

## By type

- Clearance: 30
- Courtyards overlap: 3
- Silkscreen overlap: 33
- Track width: 0

## Interpretation

The board is not DRC-clean. Clearance violations are concentrated around the USB-C footprint and dense routing. Courtyard overlaps occur between closely spaced passives and the intentionally tight J5/J6 pair. Silkscreen overlaps occur where GPIO labels are close to component bodies and pads. No track-width violations remain after widening 44 traces to 0.2 mm.