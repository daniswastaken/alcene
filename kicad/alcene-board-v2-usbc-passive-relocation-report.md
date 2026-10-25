# USB-C Passive Relocation Report — alcene-board-v2

## Task
Relocate R1, R2, C1, C2 (J2 USB-C related passives) from their crowded positions north of J2 into the empty board area between SW1 and J2, rerouting only the copper directly affected, while preserving exact schematic connectivity and strict DRC-driven development.

## Files
- PCB modified: `X:/alcene/kicad/alcene-board-v2-rebased-zero-drc.kicad_pcb` (single file, saved in place; owner handles Git recovery)
- Schematic authority: `X:/alcene/kicad/alcene-board-v1.kicad_sch` (not modified)
- Fresh netlist generated from the schematic: `.opencode/alcene-v1.nl` (KiCad s-expr)

## Electrical verification (fresh netlist)
- `R1.1 = Net-(J2-CC1)`, `R1.2 = /GND`
- `R2.1 = Net-(J2-CC2)`, `R2.2 = /GND`
- `C1.1 = /VIN`, `C1.2 = /GND`
- `C2.1 = /VIN`, `C2.2 = /GND`
On the PCB these nets are stored as `Net-(J2-PadA5)` (CC1 via J2 pad A5) and `Net-(J2-PadB5)` (CC2 via J2 pad B5), consistent with the existing board net naming. No net was renamed; no footprint, value, or footprint-library identity changed.

## Component moves
All four units are 0805 on F.Cu. Original positions (all rotation 90):
- R1: (144.995, 108.60) → new (121.700, 110.250), rotation 90
- R2: (149.900, 108.60) → new (126.200, 110.250), rotation 90
- C1: (147.800, 108.60) → new (123.000, 114.500), rotation −90 (equiv. 270)
- C2: (151.900, 108.60) → new (128.000, 114.500), rotation −90 (equiv. 270)

R1/R2 form the CC pull-down pair in the northern row; C1/C2 form the input-capacitor pair in the southern row directly below. Columns are offset so each footprint's pads, courtyards, and GND stubs interleave with ≥ 0.5 mm spacing. Orientation of C1/C2 was flipped relative to R1/R2 so that all GND pads face their respective GND rails and all CC/VIN pads face J2 or the spine drop, which kept every route short and direct.

## Final connectivity (real copper, verified after routing and again after reopen)
- **CC1 (R1.1 → J2 A5)**: pad-embedded via at R1.1 (121.7, 111.1625) → B.Cu 45° jog to y=110.4 → B.Cu lane to x=141.6 → 45° rise to (143.5, 108.5) → via → F.Cu y=108.5 → F.Cu drop at x=144.995 into J2 pad A5 (144.995, 111.84). The x=144.995 drop is the only legal entry into A5 (0.15 mm copper gaps to A4/A6 on both sides; the optional 0.15 mm-side entry is impossible at the copper level). The dimmed-away F-only options for the whole trip are blocked by the GND spine at x=141.6 (F.Cu, y=103.34…116.2) and the GND river at y=103.34, which is why CC1 hops to B.Cu once.
- **CC2 (R2.1 → J2 B5)**: pad-embedded via at R2.1 (126.2, 111.1625) → B.Cu vertical to y=114.41 → B.Cu lane east to x=147.545 → B.Cu vertical into J2 pad B5 (147.545, 113.19). B5 can only be entered from the y≈114.4 southern lane (same-lane entrance that was already in use pre-move, carried on B.Cu so the y-lane can pass under the GND spine).
- **VIN (C1.1, C2.1)**: C1.1 (123.0, 113.55) and C2.1 (128.0, 113.55) short F stubs converge on the F lane y=112.3, which terminates in a via at (121.0, 112.3) → single B.Cu vertical to (121.0, 102.013) → via placed directly on the existing F.Cu VIN spine y=102.013 (`Net-(J2-…) backbone track cd5c79`). The B.Cu passage is required because the GND river y=103.34 (x=104.16…141.49) makes any all-F vertical from the row area into the spine impossible.
- **GND**: R1.2/R2.2 (north pads) drop up via stubs into the existing GND bus y=107.688, extended west to x=121.7 and anchored T-style on the GND spine at (141.6, 107.688). C1.2/C2.2 (south pads) drop down via stubs into a new GND rail y=117.272 running from the existing SW1-junction point (111.95, 117.272) east to x=128.0. Both rails are part of the pre-existing GND copper; no isolation cuts or zone edits were used.
All connections are real copper with real endpoints (verified endpoint-by-endpoint via trace query after routing, and again via `kicad-cli` unconnected-items = 0).

## Copper edit inventory
Deleted obsolete segments tied to the old positions (15 total):
- CC1 old route: vertical x=144.995 y=109.513…111.84; B.Cu lane y=111.1625 and its diag to via2 (were auto-mislabeled `Net-(J2-PadB5)` at creation — recreated with correct net and geometry moved north so the lane no longer passes under the CC2 pad via).
- CC2 old route: B5 escape y=113.54…114.245, diag to (147.9, 114.6), lane east to (150.95, 114.6), diag to (151.4, 114.15), vertical x=151.4 to y=111.013, diag to old R2 (149.9, 109.513).
- VIN old C1/C2 feeds: y=108.6 lane pieces, diag to (147.9, 108.9), stubs to old C1/C2 pads, and the (151.75, 109.8) jog. The critical hop `(148.395, 108.6) → (152.95, 108.6)` was rebuilt so the A9 vertical keeps its top-end junction; no other pre-existing VIN copper (A4/A9/B4/B9 stitches, y=115.08 lane, x=152.95 vertical, spine) was touched.
- GND old bus east half `(141.6 → 152.4, y=107.688)`, whose east end lost its capacitor pad after the move and dangled; the kept spine/junction at (141.6, 107.688) is untouched.

New copper (21 segments + 5 vias):
- 5 VIN segments (F stubs, F lane y=112.3, B vertical x=121.0) + vias at (121.0, 112.3) and (121.0, 102.013), 0.6/0.3 through, VIN net.
- 6 GND segments (bus extension to x=121.7, two north stubs, south rail y=117.272 from (111.95,117.272), two south stubs). No vias.
- 5 CC1 segments (3 B.Cu with net-correct labels, 2 F.Cu) + vias at R1.1 pad center (121.7, 111.1625) and (143.5, 108.5).
- 3 CC2 B.Cu segments + via at R2.1 pad center (126.2, 111.1625).
- 1 rebuilt VIN hop `(148.395,108.6) → (152.95,108.6)` on F.Cu.
All via diameters are 0.6 mm with 0.3 mm drill — the smallest via already in use on this board. Via-in-pad placement was used only where the pad is on the same net and it removed a stub entirely (R1.1, R2.1).

## Silkscreen
Reference silks were repositioned to stay off the new VIN lane and the R/C courtyards:
- R1 ref: (124.05, 110.25), R2 ref: (129.60, 110.25) — between/past columns, rotation preserved
- C1 ref: (120.45, 114.50), C2 ref: (130.45, 114.50) — west of C1, east of C2
Values (`5.1k`, `10uF`, `100nF`) are F.Fab annotations that moved with the footprints; no value text was retyped or hidden. The `5V` J9 label and all board branding were not touched.

## Phase H — only intended objects changed
Footprint position/rotation audit after completion:
- Changed: R1, R2, C1, C2 only.
- Unchanged (verified identical coordinates + rotation): J2 (143.295, 111.84, 0), SW1 (111.96, 117, 90), J1 (104.16, 50, 0), J3 (129.56, 50, 0), J4 (58.21, 117.3, 90), J5 (145, 55, 0), J6 (147.54, 55, 0), J7 (130.93, 38.75, −90), J8 (111.78, 38.75, −90), J9 (147.54, 38.75, −90), MH1 (52.125, 37.85), MH2 (97.315, 37.85).
- Board outline, Alcene logo, display reservation graphics, and all unrelated silks are untouched (no graphic object was edited; visual 2D re-render confirms).

## DRC evidence (native `kicad-cli pcb drc --severity-all --format json`)
- Baseline (pre-change): `drc_cli6.json` → found 0 violations, 0 unconnected items; ERC 0/0/0.
- Intermediate run after the first full re-route: `drc_cli7.json` → 3 violations (2× shorting_items between Net-(J2-PadA5)/Net-(J2-PadB5), 1× track_dangling on the old GND bus) + 1 unconnected item. Root causes identified and fixed: (a) the two CC1 B.Cu lanes were added with the wrong net label AND geometrically ran through the CC2 pad via at (126.2, 111.1625) — replaced with the y=110.4 B.Cu reise path with correct net labels; (b) old GND bus east half deleted. The unconnected item cleared with the shorts.
- After the CC1 path rework: `drc_cli8.json` → 0 violations, 0 unconnected.
- After silkscreen adjustments: `drc_cli9.json` → 0 violations, 0 unconnected.
- After reopen/reload from the saved file: `drc_cli10.json` → 0 violations, 0 unconnected, 0 schematic-parity issues.
Final: **0 DRC errors, 0 DRC warnings, 0 unrouted connections, 0 shorts, 0 dangling copper.** No rule was weakened and no exclusion was added. Copper zones: the board has none (query_zones = 0), so no refills were required.

## ERC
`run_erc` on `alcene-board-v1.kicad_sch`: 0 errors, 0 warnings, 0 informational violations (run again after completion).

## Visual inspection
2D render (`get_board_2d_view`, layers F.Cu/B.Cu/Edge.Cuts/F.SilkS) inspected before and after every meaningful step. Final render shows the R1/R2 pair and the C1/C2 pair as a compact two-row group in the empty area between SW1 and J2, with readable, unobstructed reference silks, no residual copper at the old component positions, and all unrelated features unaltered. (3D viewer inspection not performed — outside this session's tool set; all other Phase-I checks were executed.)

## Assumptions and notes
- The board's CC net names (`Net-(J2-PadA5)`, `Net-(J2-PadB5)`) differ from the schematic's display names (`Net-(J2-CC1)`, `Net-(J2-CC2)`); net identity is positional (pads A5/B5 of J2), and the fresh netlist confirms both R1→CC1 and R2→CC2 with their GND pads on `/GND`. No rename was performed.
- Five vias were introduced; all five are justified: CC1/CC2 need to cross the GND spine wall and B5 performs a single-lane entry from the southern corridor; VIN needs B.Cu to bypass the GND river on its way to the y=102.013 spine tap. No other route on the board was touched to make room.
- The buffer via at each CC resistor sits at the resistor pad center — considered part of the direct pad connection, not a detour.
- No zones existed, so no zone refills were needed; connectivity is entirely track/pad copper.
- The intermediate DRC run (drc_cli7) reported faults that the same strict ruleset later proved fully resolved; all four post-fix runs on the saved file are clean.
