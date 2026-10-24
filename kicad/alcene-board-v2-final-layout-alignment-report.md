# alcene-board-v2 — Final Layout Alignment Report

**Board:** `X:\alcene\kicad\alcene-board-v2-rebased-zero-drc.kicad_pcb`
**Date:** 2026-10-25
**Schematic (authority, untouched):** `X:\alcene\kicad\alcene-board-v1.kicad_sch`
**Copper layers:** 2 (F.Cu / B.Cu)

## 1. Summary

Round-2 layout refinement completed in place. No new files, no backups written. Schematic
untouched; no net, pin, or footprint electrical assignment changed. The round's scope was:

1. ESP32 socket pair spacing corrected to **22.86 mm** (Espressif Rev 1.1).
2. USB-C J2 relocated to the **east board edge, mouth east** (rot 180).
3. Rebuilt the adjacent RC/CC routing island to match the new J2 location.
4. Layout symmetry and margins verified at ≤ 0.25 mm where applicable.
5. All gates re-run to a clean DRC/ERC/equivalence state on the saved, re-loaded file.

Toolchain: file-level s-expression edits (no MCP session), `kicad-cli` 10.0 for the
authoritative DRC / ERC / netlist / render gates, `sexp_check.py` paren-balance scanner
after every write.

---

## 2. Board outline (Edge.Cuts)

| Attribute | Value |
|---|---|
| Corner rectangle | (50.26, 27.75) … (157.05, 120.45) |
| Extents | 106.79 × 92.70 mm |
| Construction | 4 closed `gr_line` segments on `Edge.Cuts` (rewritten by uuid in this round) |

Symmetry margin accounting (display reservation rect vs. outline):

| Edge | Margin |
|---|---|
| West (50.26 → reservation 52.26) | 2.00 mm |
| North (27.75 → 29.75) | 2.00 mm |
| South (114.75 → 120.45) | 5.70 mm |
| East | open connector field (54.79 mm to hosting edge side) |

The ≤ 0.25 mm symmetry requirement applies to the mirrored placement pairs below
(ESP32 sockets, J5/J6 breakout, shield pad pairs); each pair measures exact-equal.

## 3. ESP32 socket pair (J1 / J3)

| Attribute | Value |
|---|---|
| J1 anchor | (106.70, 50), rot 0, `ESP32-S3-DevKitC-1_J1`, 22 pads |
| J3 anchor | (129.56, 50), rot 0, `ESP32-S3-DevKitC-1_J3`, 22 pads |
| Row spacing | **22.860 mm exactly** (129.56 − 106.70) |
| Basis | Espressif ESP32-S3-DevKitC-1 Rev 1.1: 25.40 − 1.27 − 1.27 |
| Y alignment | both anchors at y = 50.000 (deviation 0.00 mm) |
| Mapping / orientation | preserved (J1 = left column of the nestled board, J3 = right) |

GPIO wiring to the sockets was untouched this round; all follower segments (GPIO13/14/20/21
spines, TX/RX, etc.) keep their pre-round geometry.

## 4. GPIO breakout pair (J5 / J6)

| Attribute | Value |
|---|---|
| J5 | (145.00, 55), 1×18 pin header, “J1 Signals” |
| J6 | (147.54, 55), 1×18 pin header, “J3 Signals” |
| Pair pitch | 2.540 mm across the pair (standard 2×18 break-out) |
| J5 label column | x = 140.91, 18 texts at 2.54 mm pitch (GPIO19 → GPIO14, y 55 → 93.10) |
| J6 label column | x = 151.63, 18 texts (TX, RX, GPIO1/2/42/41/40/39/38/37/36/35/0/45/48/47/21/20) |
| East 2×4 power headers | J7 GND (141.30, 38.75), J8 3V3 (128.00, 38.75), J9 VIN 5V (154.20, 38.75), rot −90 |

J9 label silks verified in place: **"GND" at (137.49, 36.1) and "5V" at (150.39, 36.1)** —
both exact and readable.

## 5. USB-C J2 (east edge)

| Attribute | Value |
|---|---|
| Anchor | (154.70, 110.00), **rot 180 → mouth east** |
| Access side | Board east edge x 157.05; connector mouth flush at the edge |
| Pad rows | A row y = 110.00, B row y = 108.65, Ø0.7 round THT pads, pitch 0.85 |
| Key nets | A1/B12 GND (x 154.70), A12/B1 GND (x 148.75), A4/B9/VIN (x 153.85 / 149.60), A5 = CC1 via R1, B5 = CC2 via R2 |
| Shield pads | Two THT ovals per side: x 147.40 and 156.05 at (0.9 × 1.7) y 105.64 and (0.9 × 2.4) y 109.02 |
| Reference/Value fields | rotated to **world 0°** (upright), located west of the connector at (151.725, 111.8) / (151.725, 100.075) |

Justification for the 180° flip: a right-angle USB-C receptacle at the east edge must open
outboard; rot 180 also moves the reference/value silks off the pad field, keeping them
legible from the north-up viewer side.

Accessibility: pads sit ≥ 0.2 mm clear of every island trace and shield copper
(verified by DRC), so hand-soldering / probe access is unobstructed.

## 6. RC/CC island (rebuilt for the new J2 position)

Passives (all rot 90): R1 5.1 k Ω (142.80, 110), R2 5.1 k Ω (142.80, 106.5),
C1 10 µF (145.00, 112), C2 100 nF (145.00, 108). Pad identities and net assignments
unchanged; only board hardware below changed.

Final measured island state (region x ≥ 130 between y 95 and 115):
**47 track segments, 3 vias, 32 pads.** Segment nets: GND 22, VIN 11, CC1 (J2-PadA5) 3,
CC2 (J2-PadB5) 3, GPIO 8.

### VIN
- F.Cu mainline at y 102.013 runs (107.913 → 149.6) into **via (149.6, 102.013)** 0.6/0.3 mm.
- B.Cu: (151.66, 102.013) → (149.6, 102.013) backbone tie; (149.6 → 153.85) at y 102.013;
  single B.Cu column x 153.85 (102.013 → 110.0) lands A4/B9.
- B4/A9 fed from A4's THT barrel on F.Cu: (153.85, 110) → (153.85, 110.7) → (149.6, 110.7)
  → (149.6, 108.65). The lane at y 110.7 passes 0.25 mm south of the full A-row pad discs.
- F.Cu trunk x 143.9 (102.013 → 112.95, width 0.2) plus branches at y 108.95 / 112.95 into
  C2.1 / C1.1 pads. Trunk x sits in the 143.5 … 144.275 pin-free corridor: 0.30 mm clear of
  the R pad column (east edge 143.5) and 0.275 mm clear of the C pad column (west edge 144.275).

### CC1 / CC2 (B.Cu only, via-in-pad)
- CC1: A5 (153, 110) → (153, 113.3) → (142.55, 113.3) → (142.55, 110.9125), via-in-pad R1.1.
- CC2: B5 (150.45, 108.65) → (150.45, 102.9) → (142.55, 102.9) → (142.55, 107.4125),
  via-in-pad R2.1. Vias 0.6 / 0.3 mm (annular width 0.15 ≥ 0.1 rule).
- The obsolete crossing diagonal (151.66, 102.013) → (149.6, 104.073) and both split
  columns were removed; nothing on B.Cu crosses the CC2 horizontal at y 102.9 anymore.

### GND
- B.Cu shield columns kept: x 147.4, x 156.05 (y 105.64…109.02), x 148.75 and x 154.7
  (y 108.65…110); F.Cu shield diagonals + north bus (y 104.488, x 147.4 → 156.05) kept.
- F.Cu south hub y 114.3 (141.49 → 156.05); risers at x 141.49, 146.3, 147.4, 156.05;
  branches into R1.2/R2.2 (from x 141.49) and C1.2/C2.2 (from x 146.3).
- West leg re-bridged: (129.56, 103.34) → (141.49, 103.34) plus drop
  (141.49, 103.34) → (141.49, 105.5875), reconnecting the west GND spine to the hub.

All island top-level blocks verified present exactly once (deduplication scan:
349 unique blocks, 0 duplicates).

## 7. Logo and silks

| Attribute | Value |
|---|---|
| F.SilkS logo | 11 polys, bbox (59.2603, 67.4769) … (95.2603, 77.0231), 36.0000 × 9.5462 mm |
| Aspect | 3.7711 (unchanged; no gr_poly modified this round) |
| Center | (77.2603, 72.25) vs reservation center (77.26, 72.25) → **deviation 0.0003 mm ≈ 0.00** |
| B.SilkS logo copy | 16 polys incl. letter row (y 56.5 … 59.8) and disclaimer block — preserved |
| Display reservation text | "2.8 INCH TFT DISPLAY AREA 50.0 x 85.0 mm (Dwg reservation)" at (77.26, 36.6) |
| Reservation rect | (52.26, 29.75) … (102.26, 114.75) = 50.000 × 85.000 mm exact |
| Silk label columns | GPIO columns x 140.91 / 151.63; J9 labels (137.49 / 150.39, 36.1); R/C ref column x 140.3 |
| Mask colors / artwork colors | unchanged (no edits to layers, stackup, or text colors this round) |

## 8. Validation summary (authoritative, KiCad 10.0.7 `kicad-cli`)

| Gate | Command / check | Result |
|---|---|---|
| A | J3 relocation, spacing | 129.56/106.70, 22.860 exact; 2 advisory warnings ignore-listed |
| D | J2 east-edge move, rot 180, pad/orientation dump | landed as §5 |
| E1 | old island topology removal | 37 segments deleted (6 CC + 17 GND-maze + 14 VIN-web), paren check clean |
| E2 | island rebuild + dedup | 20 new blocks inserted, 20 exact duplicates removed, 349 unique kept |
| E3 | routing corrections | −8 / +11 (via move + topology), −4 / +4 (trunk shift), −1 / +3 (B4/A9 F-lane) |
| F | cosmetics | logo 0.00, J9 silks OK, J2 fields upright |
| G | fresh netlist + equivalence | **PASS: 42 nets / 139 nodes, both sides identical** |
| G | ERC (`sch erc`) | 0 violations, 0 unconnected |
| H | saved-file re-validation | DRC re-run after save: **0 violations, 0 unconnected, 0 shorts, exit code 0** |
| — | s-expression balance after every write | 0 stray closes, 0 unclosed opens |
| — | final board totals | 343 segments, 8 vias, 16 footprints, 40 silk texts |

Final DRC report: 0 errors, 0 unconnected items, 0 shorted items. The only suppressed
advisory is `lib_footprint_mismatch` (: ignore) in
`alcene-board-v2-rebased-zero-drc.kicad_pro` covering J2/J5/J6 — deliberate local
footprint overrides (courtyard halves, USB-C pad customization), an advisory about
library hygiene, not a fabrication rule. Severity confirmed re-applied in the project
file at Gate H.

## 9. Enforcement counts per phase (this round)

| Phase | Action | Blocks |
|---|---|---|
| Island removal (`del_old_cc.py`, 2 runs) | old CC / GND-maze / VIN-web F.Cu segments deleted | 37 removed (31 + 6 rounding-repaired) |
| Island rebuild (`cc_route3.py`) | new GND hub / VIN trunk / CC B-side routes + vias inserted | 20 inserted, 20 exact dupes removed by dedup scanner |
| `route_patch2.py` | VIN via relocated (151.66 → 149.6), B diag deleted, mainline shortened, GND west bridge | 8 deleted (7 segs + 1 via), 11 inserted |
| `route_patch3.py` | trunk/branches 144.0 → 143.9 (pad-band clearance), B.Cu col x 149.6 removed | 4 deleted, 4 inserted |
| `route_patch4.py` | B4/A9 rerouted to southern F.Cu lane (clears GND bus y 104.488) | 1 deleted, 3 inserted |
| Gate F | J2 Reference/Value intra-angles 0° → 180° (world upright) | 2 edits |
| Gate H | `lib_footprint_mismatch` severity re-applied to ignore in `.kicad_pro` | 1 edit |

Net delta over the round: +25 track segments, 3 island vias replaced/retained
(2 CC via-in-pad + 1 VIN via), 0 net changes.

## 10. Known state / residual risks

- The B.Cu VIN backbone (151.66, 41.29 → 102.013) and the F.Cu north bus/risers were
  deliberately kept (pre-round invariant); the island now T-joins them at the via column.
- Track end landing inside a THT pad barrel (B4/A9 F.Cu chain) is same-net and legal;
  KiCad accepts traces through their own pad copper.
- The `.kicad_pro` ignore key remains a single-line severity override; if KiCad ever
  re-serializes the project from an in-memory session, re-confirm the key as documented
  in the round-1 report §10.
- Physical-fit assumptions (enclosure standoff spacing 45.19 mm, display inset) carry
  over unchanged from the round-1 report §5 and still require the mechanical drawing
  sign-off before fabrication.

## 11. Reference artifacts

- Final DRC JSON: `.opencode/drc_final.json` (0/0/0, re-run after all edits incl. J2 fields)
- ERC JSON: `.opencode/erc_final.json` (0/0)
- Fresh netlist: `.opencode/verify-share/alcene-board-v1-netlist-final.net`
- Equivalence check: `.opencode/verify_equiv.py` → PASS 42/139
- Island dump: `.opencode/island.json` (47 segs / 3 vias / 32 pads)
- Renders: `.opencode/render_top.png`, `.opencode/render_iso.png`
