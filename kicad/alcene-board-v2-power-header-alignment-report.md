# Power Breakout Header Alignment — Surgical Round 3 Report

**Board:** `X:\alcene\kicad\alcene-board-v2-rebased-zero-drc.kicad_pcb`
**Schematic (authority, unmodified):** `X:\alcene\kicad\alcene-board-v1.kicad_sch`
**Date:** 2026-10-25
**Method:** KiCad file-coordinate measurement (settled rotation matrix verified against raw pad data and existing track endpoints; extents were not estimated from pixels).

---

## 1. Objective and result

Horizontal-only repositioning of the three 2×4 power breakout headers (J8 3V3, J7 GND, J9 5V/VIN) so that:

- the 3V3 header's left edge is flush with J1's left edge,
- the 5V header's right edge is flush with J6's right edge,
- the GND header sits between them with equal edge-to-edge gaps,

plus silkscreen labels moved with their headers and local copper rerouted. Result: **achieved exactly, with strict zero-DRC retained.**

---

## 2. Measured geometry before → after (authoritative file coordinates)

Physical footprint extents used: F.Fab body outline of each footprint (corroborated by pad-copper extents; both given below). For these footprints (rot −90, identical 2×4 libraries):

- header fab X-span = `[anchor − 8.89, anchor + 1.27]` (width 10.16 mm),
- header pad X-span = `[anchor − 8.47, anchor + 0.85]`.

J1 (rot 0) fab X = `[105.43, 107.97]`, pads X = `[105.85, 107.55]`.
J6 (rot 0) fab X = `[146.27, 148.81]`, pads X = `[146.69, 148.39]`.

### 2.1 Header anchors (X only; Y and rotation untouched)

| Header | Role | Anchor X before | Anchor X after | ΔX | Fab X after | Pads X after |
|---|---|---|---|---|---|---|
| J8 | 3V3 | 128.00 | 114.32 | −13.68 | 105.43 … 115.59 | 105.85 … 115.17 |
| J7 | GND | 141.30 | 130.93 | −10.37 | 122.04 … 132.20 | 122.46 … 131.78 |
| J9 | 5V (net /VIN) | 154.20 | 147.54 | −6.66 | 138.65 … 148.81 | 139.07 … 148.39 |

### 2.2 Required alignment equations — measured AFTER the move

| Requirement | Left value | Right value | Difference |
|---|---|---|---|
| L(3V3) = L(J1), fab | 105.43 | 105.43 | **0.00 mm** |
| L(3V3) = L(J1), pads | 105.85 | 105.85 | **0.00 mm** |
| R(5V) = R(J6), fab | 148.81 | 148.81 | **0.00 mm** |
| R(5V) = R(J6), pads | 148.39 | 148.39 | **0.00 mm** |

### 2.3 Equal-gap requirement around GND — measured AFTER the move

| Gap (fab bodies) | Value | Gap (pad copper) | Value |
|---|---|---|---|
| L(GND) − R(3V3) = 122.04 − 115.59 | **6.45 mm** | 122.46 − 115.17 | **7.29 mm** |
| L(5V) − R(GND) = 138.65 − 132.20 | **6.45 mm** | 139.07 − 131.78 | **7.29 mm** |

Both measures agree on equality because all three headers are geometrically identical libraries.

### 2.4 Silkscreen labels (top-level `gr_text`, F.SilkS)

| Label | Before (x, y, rot) | After (x, y, rot) | Moved by | Centered over header |
|---|---|---|---|---|
| 3V3 | 124.19, 36.1, 0 | 110.51, 36.1, 0 | −13.68 (Δ identical to J8) | yes (110.51 = (105.43+115.59)/2) |
| GND | 137.49, 36.1, 0 | 127.12, 36.1, 0 | −10.37 (= Δ J7) | yes (127.12 = (122.04+132.20)/2) |
| 5V | 150.39, 36.1, 0 | 143.73, 36.1, 0 | −6.66 (= Δ J9) | yes (143.73 = (138.65+148.81)/2) |

No duplicate or leftover label text exists; the labels keep Y = 36.1 and rotation 0. In-footprint Reference/Value fields moved automatically with their footprints and were not edited.

---

## 3. Electrical verification

- Pad-to-net mapping unchanged (measured from the saved file): J8 all 8 pads = `/3V3`; J7 all 8 pads = `/GND`; J9 all 8 pads = `/VIN` (visible label stays "5V"; the net name was **not** renamed).
- Fresh netlist exported from `alcene-board-v1.kicad_sch` (`: .opencode/verify-share/alcene-board-v1-netlist-final.net`): schematic **42 nets / 139 nodes**, board **42 nets / 139 nodes**, both sides identical → **EQUIVALENCE: PASS** (`.opencode/verify_equiv.py`).
- Connectivity is physical, not name-deep: rerouted copper actually lands on the moved pads (real track segments; DRC ratsnest reports 0 unconnected). No graphical imitations, no dangling segments, no splices onto foreign nets.

### 3.1 Copper rerouted (only what the horizontal moves made necessary)

Track segment census: 343 → **329** segments (−28 old, +14 new), vias 8 unchanged, same positions/nets.

- **3V3 (J8):** deleted 10 old-row/feed segments, inserted 4: F.Cu rows y 38.75 and y 41.29 (106.7 → 114.32), B.Cu east column x 114.32, B.Cu feed (106.7, 50) → (106.7, 41.29) landing on J1 pin 1 (`(106.7,50)`, 3V3).
- **VIN (J9):** deleted 7 old-row/col segments, inserted 4: F.Cu rows y 38.75/41.29 (139.92 → 147.54), B.Cu column x 147.54, B.Cu tie (147.54, 41.29) → (151.66, 41.29) landing on the pre-existing VIN backbone top end. Backbone, island, mainline, and via (149.6, 102.013) untouched.
- **GND (J7):** deleted 11 old-row/col/feed segments, inserted 6: F.Cu rows y 38.75/41.29 (123.31 → 130.93), B.Cu column x 130.93, B.Cu feed from J3 pin 1 `(129.56,50)` = GND: (129.56, 50)→(129.56, 44.31)→(123.31, 44.31)→(123.31, 41.29). The feed corridor (y ≈ 44.31) clears J7 pads (2.07 mm) and is layer-separated from J9's rows.

Zone refill: the board contains **0 zone objects**, so zone refill is a no-op (recorded; nothing to refill).

---

## 4. DRC-driven step gates (fresh `kicad-cli pcb drc` after every step, `--severity-error --severity-warning --exit-code-violations`)

| Gate | Errors | Warnings | Unconnected | File |
|---|---|---|---|---|
| 1. Baseline (before any move, after zone audit) | 0 | 0 | 0 | `.opencode/drc_power_baseline.json` |
| 2. After J8 move + 3V3 reroute | 0 | 0 | 0 | `.opencode/drc_power_step2.json` |
| 3. After J9 move (before GND move) | 58 | — | 0 | `.opencode/drc_power_step3.json` (audit artifact) |
| 4. Repair: J7 move + GND reroute (J9's west pads had landed on J7's old position; the spec's step ordering required J9=147.54 before the pair could clear. Cause identified, repaired, re-gated.) | 0 | 0 | 0 | `.opencode/drc_power_step4.json` |
| 5. Final (fresh DRC on saved file = reload-from-disk test; kicad-cli parses the file anew each run) | 0 | 0 | 0 | `.opencode/drc_power_final.json` |

- No rule, clearance, severity, or net assignment was changed; `alcene-board-v2-rebased-zero-drc.kicad_pro` was not modified (still contains the pre-existing `lib_footprint_mismatch: ignore` advisory setting).
- Every run parsed the saved file from disk, which doubles as the reload-stability check (five independent loads all returned the same result).
- ERC on the schematic: **0 errors, 0 warnings** (`.opencode/erc_power_final.json`, EXIT=0).
- S-expression sanity: `sexp_check.py` — 0 stray closes, 0 unclosed opens after every edit; `duplicates.py` — 0 duplicates (segment census 329 consistent with 343−28+14).

---

## 5. Movement audit — only authorized objects moved

All 16 footprint anchors compared before/after from the saved file:

- Changed: **J8 only** (128 → 114.32), **J7 only** (141.3 → 130.93), **J9 only** (154.2 → 147.54). Y and rotation −90 preserved for all three.
- Unchanged: J1 (106.7, 50), J2 (154.7, 110, 180), J3 (129.56, 50), J4 (60.75, 113.25, 90), J5 (145, 55), J6 (147.54, 55), SW1 (114.5, 117, 90), R1 (142.8, 110, 90), R2 (142.8, 106.5, 90), C1 (145, 112, 90), C2 (145, 108, 90), MH1 (54.665, 32.25), MH2 (99.855, 32.25).
- Unchanged: board outline, 50×85 mm display reservation, alcene logo, all other silkscreen (GPIO column x 140.91, J6 column x 151.63, R/C ref silks intact).
- Only the three named `gr_text` labels moved. Copper blocks changed are exactly the 28+14 enumerated in §3.1.
- Schematic file untouched (verified by fresh export matching the board).

Even the intermediate audit violation set (§4 gate 3) is documented so the process remains fully reconstructable via Git.

---

## 6. Visual inspection (2D-ish top render + isometric 3D render)

- Top view: three headers on one common row (y unchanged); 3V3 flush above J1's left edge; 5V right edge flush with J6's right edge; GND visibly centered; labels "3V3", "GND", "5V" centered above their headers; no leftover text; no footprint overlap (J1/J3/J5/J6 columns and courtyards clear the header row band y 36.98…43.07 with ≥ 5.16 mm to the sockets' courtyard band starting y 48.23).
- Iso view: no mechanical collision; all three power headers clear of the ESP32 socket housings and of the display reservation.
- Renders saved: `.opencode/render_top_round3.png`, `.opencode/render_iso_round3.png`.

---

## 7. Acceptance summary (strict zero-DRC criteria)

| Criterion | Status |
|---|---|
| Zero DRC errors | **0** ✅ |
| Zero DRC warnings | **0** ✅ |
| Zero unresolved violations | **0** ✅ |
| Zero unrouted connections | **0** ✅ |
| Zero unintended shorts / dangling copper | **verified** ✅ (shorting_items = none in final run; deleted-block census clean) |
| L(3V3) = L(J1) | **0.00 mm** ✅ |
| R(5V) = R(J6) | **0.00 mm** ✅ |
| Gaps around GND equal | **6.45 / 6.45 mm (fab)**, **7.29 / 7.29 mm (pads)** ✅ |
| Labels centered, single instance each | ✅ |
| Only authorized objects moved | ✅ (anchor audit §5) |
| Schematic unchanged, mapping intact (42/139 PASS) | ✅ |
| Eliminate ERC | **0 / 0** ✅ |

**The save meets every mandatory condition.**

---

## 8. Notes and carried-over residuals

- Step-3 gate: J9 landed at its exact target while J7 still sat at its old spot (the spec prescribes the J9 step before the GND-centering step) — the pair data-locked. Resolution followed the spec's own DRC-driven stop-and-repair rule: applied the authorized GND move (already part of the plan) immediately, so the final and step-4 gates are clean 0/0.
- ESP32 socket row spacing: board is at 22.86 mm (matches genuine Espressif ESP32-S3-DevKitC-1 per official dimension drawing `DXF_ESP32-S3-DevKitC-1_V1.1_20220429`: 25.40 board width, strips inset 1.27 each side). The module the owner intends to plug measures ~28.4 mm wide with 25.4 mm pin-row centers — third-party clone geometry. A 25.4 adapter decision was deferred: if adopted later, J3 anchor moves 129.56 → 132.10 with a full reroute of the J3 half of the GPIO fan and J3 GND/VIN feeds. Verify the chosen module family before any future rework.
- `.kicad_pro` GUI-serialization fragility (from round 2) still applies if the project is opened and re-saved in the CAD GUI: the advisory `lib_footprint_mismatch: ignore` key should be re-checked after any such re-save.
- Mechanical-fit assumptions from round 2 (standoff spacing) are unchanged and remain unverified here.
- Measurement tooling: `.opencode/step1_facts.py` (full facts dump; note its −90° footprint X-extent printout is mirrored by a known display bug in that helper — trust the raw-data matrix used in this report, which was verified against raw pad coordinates and track endpoints), `sexp_check.py`, `duplicates.py`, `verify_equiv.py` in `.opencode/`.
