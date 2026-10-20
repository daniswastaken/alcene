# alcene-board-v1 ERC Report — Final Revision

- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- KiCad version: 10.0.7
- Date: 2026-10-20
- Machine-readable report: `X:\alcene\kicad\erc-fresh.json`

## Result

- Errors: 0
- Warnings: 0

## Notes

The previous nine `multiple_net_names` warnings were removed by deleting redundant electrical alias labels on shared TFT nets. TFT functions are now documented with non-electrical text. Electrical connectivity is unchanged.

Ignored checks remain:
- `single_global_label`
- `four_way_junction`
- `simulation_model_issue`
- `footprint_filter`

## ERC limitations

ERC does not establish:
- Physical connector fit.
- Correct current rating.
- Measured voltage stability.
- Power-source behavior outside the documented operating restrictions.