# alcene-board-v1 ERC Report

- KiCad version: 10.0.7
- Date: 2026-10-20
- Source: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- Machine-readable report: `X:\alcene\kicad\erc-fresh.json`

## Result

- Errors: 0
- Warnings: 9
- Ignored checks: `single_global_label`, `four_way_junction`, `simulation_model_issue`, `footprint_filter`

## Warnings

All warnings are `multiple_net_names`:
1. GPIO10 and LCD_CS
2. GPIO8 and LCD_RST
3. GPIO9 and LCD_DC
4. GPIO12 and LCD_CLK
5. 3V3 and LCD_BL
6. GPIO14 and TOUCH_CS
7. GPIO11 and TOUCH_DIN
8. GPIO13 and TOUCH_DOUT
9. GPIO15 and TOUCH_IRQ

## Interpretation

ERC passes with no errors. The warnings are net-name aliases on shared nets; the final netlist resolves each to one name. They do not indicate shorts or missing connections, but they should be cleaned for documentation clarity.