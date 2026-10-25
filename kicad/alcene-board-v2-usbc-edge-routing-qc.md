# Round 4 QC — USB-C (J2) south-edge flush mount + rebuild

Target: `alcene-board-v2-rebased-zero-drc.kicad_pcb` (in-place edit only; no backups created).
Authority schematic `alcene-board-v1.kicad_sch` unchanged; ERC green (see gates).

## Result summary

| Gate | Result |
|---|---|
| DRC (kicad-cli 10.0, project defaults) | **0 errors / 0 warnings / 0 unconnected** (.opencode/drc_op2.json) |
| ERC (kicad-cli 10.0) | **0 violations / 0 unconnected** (.opencode/erc_op2.json) |
| Schematic↔board net equivalence | **PASS — 42 nets / 139 nodes, identical both sides** (.opencode/verify_equiv.py) |
| Duplicate segment/via scan | 0 removed (nothing to remove) (.opencode/duplicates.py) |
| S-expression balance | 0 stray closes / 0 unclosed (.opencode/sexp_check.py) |
| 45°/straight audit, rebuilt region | 0 non-45° segments |
| Anchor integrity (J1, J3–J9, SW1, MH1/MH2) | unchanged (position+rotation identical) |
| Copper totals | 329 → 320 segments; 8 → 7 vias; 2 layers only (F.Cu/B.Cu); 0 zones |

## J2 (USB-C, GCT USB4085 top-mount dip type)

- Anchor `(at 143.295 114.39)` rotation **180 → 0**, mouth plane (footprint local y 6.1) sits 0.04 mm south of
  board outline y=120.45 — flush with the south edge, mouth outwards (cable exits south, over the clear
  plug path below the edge).
- Aperture (pin window) center x 146.27 — exactly the J5/J6 GPIO bank center; body py top 113.83 leaves the
  passives row north of it.
- A/B pad rows at world y 114.39 / 115.74, pitch 0.85; shell pads (SH) at (141.945/150.585, 115.37) and
  (141.945/150.585, 118.75). All THT legs modeled with r 0.35 + pad clearance 0.15.
- Footprint silk trimmed **necessarily**: the three GCT lip silks (two side lines local y 6..8.73 and the
  bottom line y 8.73) live south of the now-flush edge and belong to the overhang that no board silk can
  reach (physical impossibility). Deleted: fp_lines (−1.62,8.73)−(7.57,8.73), (−1.62,6..8.73),
  (7.57,6..8.73). The two short later ticks (local y 2.4..3.3) and the top line y −0.68 (world 113.71) stay;
  remaining silk is ≥0.22 from the nearest pad and inside the outline.
- Value "USB-C Input" (F.Fab, world 146.27,124.32) and "PCB Edge" (Dwgs.User, 146.27,120.49) ride with the
  footprint as before; the F.Fab edge-plane detail line (local 6.1 → world 120.49) is fab-layer only — no DRC
  rule, purely mechanical documentation.
- Reference relocation (allowed by the text clause): J2 ref previously flipped by the 180° footprint text
  setup and would have sat on the passives row; moved to east of the copper column at world (153.9, 109.9),
  rotation 0, `(at 10.605 -4.49 0)`.

## Passives row (R1/R2/C1/C2)

Row y = **111.5** rot 90 (pin-1 south). Chosen so every courtyard bottom (R ±1.68 / C ±1.7 in rotated local
x) clears J2's courtyard top (y 113.33) by 0.13–0.15 mm, and the GND bus y 110.77 still passes through all
four pin-2 pads:

- R1 (144.995, 111.5) — CC1 pin-1 at (144.995, 112.4125), straight vertical from A5.
- C1 (147.8, 111.5) — shifted east of the first plan (146.9) because the first build's courtyard gap
  R1↔C1 was −0.03 (flagged) and C1's pin-1 sat inside J2's reference text box.
- R2 (149.9, 111.5) — stayed east of 149.5 so A9's north vertical keeps 0.705 to the pad column.
- C2 (151.9, 111.5).
- Reference texts repositioned to clear every pad/silk ("R1" 144.5,109.2 • "R2" 150.0,109.2 • "C1" 142.6,113.1
  • "C2" 154.4,108.3); first build had R1 ref over the west SH pad and C2 ref over C1 pin-2 — both fixed.

## Rebuilt topology (all segments 0.2 mm unless noted; 45° diagonals only)

VIN (F.Cu):
- mainline end feed (149.6,102.013)→(152.95,102.013); single east column x 152.95 down to y 117.55.
- west channel y 111.5 (x 147.9→152.95), T-joint feeding: A9 north vertical x 148.395 (111.5→114.39),
  C1 branch x 147.9 (111.5→112.45) + SW diag →(147.5,112.85), C2 SE diag (152.95,111.5)→(151.75,112.7).
- A4 fused to B9 via column bridge (148.395,114.74)−(148.395,115.39) [fuses A9/B4]; A4/B9 col bridge
  (144.145,114.74)−(144.145,115.39); B9 south escape (144.145,116.09)→(144.145,117.55) + corridor to the
  east column.

CC1 0.3: A5 (144.995,114.39) → R1 pin-1 (144.995,112.4125) — straight.
CC2 0.3: B5 south vertical (147.545,116.09→117.05), east corridor y 117.05 → x 151.4, north lane to y 113.47,
west step →(150.9,113.47), SW diag →(149.9,112.47) into R2 pin-1. Lane/corridor run 0.215 past the east SH
pad column and 0.55 below its northern tip (first build's y 114.0 lane violated SH pad-1 clearance by 0.091 —
DRC-verified, moved down).

GND (both layers, no gaps in the y110.77 bus — nothing crosses it any more):
- bus F y 110.77 x 141.6→152.4 through all four pin-2 pads; spine F x 141.6 w 0.5 (y 103.34→118.3, merges the
  SH-west pads and both edge bonds); A1/B12 west bonds into the SH-west copper, A12 east bond into SH-east.
- mainline extension (141.49,103.34)→(144.6,103.34); new via (144.6,103.34) size 0.6 drill 0.3 (values copied
  from the existing via (149.6,102.013)); B.Cu lane (144.6,103.34)→(150.585,103.34)→(150.585,118.2) hitting the
  SH-east pads; B1 bond on B.Cu (149.245,115.74)→(150.585,115.74) (F-side diagonal was dropped after a
  grazing check against the CC2 corridor).

First-build fixes worn forward: no vertical trunks into C-pin-2 pads that are already in the same column, no
NE diagonals into the A9 horizontal, no inter-row pinch below 0.65, no strip south of the SH blobs, no B.Cu
under the SH blobs.

Deleted (from the J2-local island + reuse of the old GCT geometry): 34 exact-tuple segments + 2 vias
(142.55,110.9125)/(142.55,107.4125) in op1, plus the orphan island tail (155.07,109.02)−(156.05,109.02) in
op2 (its neighbours were already deleted; it was the last 0.98 mm floating island on GND).

## Visual proof

`.opencode/r8.png` — 3D render (kicad-cli pcb render, top side, pivot 4.3,−4.5 cm): USB-C mouth exits flush
through the south board edge; C1/R1/R2 or C2 row sits north of the connector; labels readable, no silk over
pads.

## Evidence files

- .opencode/drc_op2.json, erc_op2.json — final gates (fresh, post-op2)
- .opencode/drc_usbc_base.json, erc_usbc_base.json — round-4 baselines (pre-op1)
- .opencode/drc_op1.json — first build (14 violations + 1 unconnected: 2 SH-pad clearance, 5 courtyard,
  4 silk-over-copper, 2 silk-clip, 1 dangling island tail) — fixed by op2
- .opencode/build_op1.py, build_op2.py — both edit passes (idempotent, abort-on-missing-tuple)
- .opencode/sexp_check.py, duplicates.py, verify_equiv.py — gate scripts
- .opencode/r8.png — render

## Round 5 (op3) — mating-mouth plane exactly on outline y=120.45

User saw the round-4 render: the connector visibly protruded — its mating mouth (footprint front face,
local y 8.61) sat 2.55 mm south of the edge because GCT's "PCB Edge" datum (local 6.1) was used as the flush
plane. Demand: mouth precisely at the edge, neither over nor short.

- J2 anchor `(at 143.295 114.39)` → **(143.295, 111.84)** (2.55 mm north); x unchanged (aperture centre 146.27
  still on the J5/J6 bank centreline). Front face (local 8.61) now lands at exactly world y 120.4500 —
  flush with the south outline, zero overhang, zero recess. Delta verified 0.0000 (audit5.py).
  Note: GCT's own mount datum wants the edge at local 6.1; this user-directed mounting is 2.51 mm deeper
  than spec — the shell's front lip hovers instead of capping the edge. Solder legs + shell tabs all remain
  on the board (they live at local ≤ 4.36, ≤ 116.2) so electrical and mechanical anchoring are intact.
  The footprint's "PCB Edge" dwgs text rides to world (146.27, 117.94) and the "USB-C Input" value text to
  (146.27, 121.765) — fab/dwgs layers only, no DRC rule applies there.
- Passives row 111.5 → **108.6** (R1 144.995, R2 149.9, C1 147.8, C2 151.9, rot 90): J2's fab body top edge
  (local −0.56 → world 111.28) would otherwise swallow the row. Courtyard bottoms (R 106.92 / C 106.9) now
  clear J2's courtyard top (110.78) by ~0.5 mm. Reference texts ride with the anchors (no property edits);
  world: R1 (144.5,106.3), R2 (150.0,106.3), C1 (142.6,110.2), C2 (154.4,105.4), J2 (153.9,107.35).
- GND bus y 110.77 → **107.6875** (through all four pin-2 pads: R ±0.9125 exact, C ±0.95 straddled); no gaps —
  east end x 152.4 stays 0.35 short of the VIN column x 152.95.
- 23 of the 26 J2-cluster segments rewritten in place (same uuids, count stays 320 segs / 7 vias; 3 kept:
  via feed 149.6,102.013→152.95, west GND ext, B.Cu rail). Key placements:
  - VIN: channel y 108.6 (squeezes through the R2/C1/C2 pad gap band 108.2..109.0 with 0.3 clearance each
    side); A9 vertical x 148.395 108.6→111.84; inter-row bridges (148.395 / 144.145, 112.19..112.84); B9
    escape 113.54→115.08; corridor y 115.08 midway between SH-east pad bottom 114.02 and pad top 115.35
    (gaps 0.96 / 0.17); C1 branch 147.9 → diag into pin-1 oval; C2 diag (152.95,108.6)→(151.75,109.8);
    column truncated to y 115.08.
  - CC1 0.3: A5 (144.995,111.84) → R1 pin-1 (144.995,109.5125), straight.
  - CC2 0.3: B5 south escape (147.545, 113.19→114.6), corridor y 114.6 (0.43 / 0.6 clear of the SH-east
    pads), north lane x 151.4 (0.215 past the SH pad column, as proven in round 4), west step at
    y 110.5125, SW diag into R2 pin-1 (149.9,109.5125).
  - GND: A1/B12 west bonds (142.0, 111.84 / 113.19 — endpoints inside SH-west pad-1 copper), A12 east bond
    (150.585,111.84), B1 bond B.Cu (149.245→150.585, 113.19), spine x 141.6 shortened to 116.2 (SH-west
    pad-2 centre; merges into that pad), B.Cu lane shortened to 116.2 (SH-east pad-2 centre).
- Gates (all fresh):
  - DRC kicad-cli 10.0 **0 errors / 0 warnings / 0 unconnected / 0 parity** (.opencode/drc_op3.json)
  - ERC **0 violations / 0 unconnected** (.opencode/erc_op3.json)
  - verify_equiv **PASS — 42 nets / 139 nodes identical** (unchanged from round 4)
  - sexp balance ok, duplicates 0, 45°/straight audit 0 bad, anchor integrity PASS (J1, J3–J9, SW1, MH1/MH2
    untouched)
- Visual proof: .opencode/r9.png (3D top-tilt: mouth on the edge, row north) and .opencode/r10.png (front
  profile: mating face coplanar with the board edge; the small tips below the edge are the bare THT leg
  ends, which pin through every connector tip).
