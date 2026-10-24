# Clearance disposition - alcene-board-v2 (rebase, zero-DRC)

Date: 2026-10-24
Board: `X:\alcene\kicad\alcene-board-v2-rebased-zero-drc.kicad_pcb`
Final DRC result: **0 errors, 0 warnings** (report: `alcene-board-v2-final-drc-report.txt`).

## 1. Board-wide rules (unchanged, no weakening)

| Rule | Board value |
|---|---|
| Netclass clearance | 0.2 mm |
| Min track width / all tracks | 0.2 mm (329/329 segments) |
| Via size / drill | 0.6 / 0.3 mm (4 vias) |
| Min through drill | 0.3 mm |
| Hole-to-hole min | 0.25 mm |
| Copper-to-edge | 0.5 mm |

No custom `.kicad_dru` file is shipped (the development-time rule file was
removed; the shipped file carries its final values in-board).

## 2. The one scoped exception: USB-C (J2) pad-local clearance 0.15 mm

The J2 footprint `Connector_USB:USB_C_Receptacle_GCT_USB4085` has a
0.85 mm B-side / A-side pad pitch.  Adjacent pads of *different nets*
(GND/VIN, CC1/CC2, D+/D- pairs) measure a real copper gap of
**0.85 - 0.70 = 0.15 mm** - a property of the GCT USB4085 connector
itself, not a layout choice.  With only the global 0.2 mm rule applied,
the KiCad DRC engin flagged 28 such J2-internal pad-to-pad pairs.

Disposition applied: each of the **20 pads** of J2 (16 signal + 4 shell)
carries an in-board pad-local attribute `(clearance 0.15)`.  KiCad
resolves a pad-to-pad clearance requirement as the **max** of both pads'
local clearances, so:

- J2 pad vs J2 pad requirement -> 0.15 mm, satisfied by the real 0.15 mm gap.
- J2 pad vs *anything else* -> max(0.15, 0.2) = **0.2 mm** (board rule intact).

This is a standard KiCad footprint feature (footprint authors set local
pad clearances for exactly this situation) and is kept inside the shipped
file, so **any** DRC runner (GUI, `kicad-cli`, MCP backends) sees it.
No severity overrides, no suppressions, no zone/track hackery.

## 3. Fabricator capability (JLCPCB, "2-layer economy" class)

Published JLCPCB capability values verified by web query on 2026-10-24
(sources: https://jlcpcb.com/capabilities/pcb-capabilities/ and the
publicly shared JLCPCB 2-layer Eagle `.dru` rule packs):

| JLCPCB published line | Value | Our worst case | Verdict |
|---|---|---|---|
| Min track width / spacing (1 oz, 1-2 layer) | 0.10 / 0.10 mm | 0.2 / >=0.15 | OK |
| (older community DRU floor, commonly cited) | 0.127 mm | same | OK |
| SMD pad-to-pad clearance, different nets | 0.15 mm | 0.15 (J2 only) | OK at limit |
| **PTH pad hole-to-hole spacing** | **0.45 mm** | **0.45** (J2, drilled 0.4 @0.85 pitch) | **at minimum - exact** |

The J2 hole-to-hole value is the *physical footprint geometry*
(0.85 pitch, 0.4 drill) and equals the JLCPCB 0.45 line **exactly**,
i.e. with zero margin.  Fabrication at this value is inside the
published envelope but has no headroom; order review must not round the
drill up.  This is flagged as a residual risk in the QC report.

## 4. Measured numbers

- J2 pitch 0.85 mm; pad copper dia 0.7 mm; drill 0.4 mm.
- Worst pad-edge gap (J2 adjacent, different nets): 0.15 mm.
- Worst hole-to-hole (J2 adjacent): 0.45 mm ( = JLCPCB minimum, exact).
 Everywhere else the tightest real gap measured in DRC is >= 0.2 mm.
