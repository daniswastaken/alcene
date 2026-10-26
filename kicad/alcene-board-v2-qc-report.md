# Alcene Board v2 — Thorough QC Report (electrical, JLCPCB, schematic parity)

**Date:** 2026-10-26
**Board under test:** `alcene-board-v2-rebased-zero-drc.kicad_pcb`
**Electrical authority:** `alcene-board-v1.kicad_sch`
**Method:** read-only QC. The board file was **not modified**.

---

## 1. Verdict

| Area | Result |
|---|---|
| Native DRC (`kicad-cli pcb drc --severity-all`) | **PASS** — 0 violations, 0 unconnected (`.opencode/drc_cli23.json`) |
| Native ERC (`kicad-cli sch erc --severity-all`) | **PASS** — 0 violations (`.opencode/erc-cli1.json`) |
| Schematic ↔ PCB parity (manual, partition-based) | **PASS** — all 14 components, every pin, every value, every footprint identical; 0 differences |
| Electrical function review | **PASS** — power tree, USB-C power roles, reset switch, TFT mapping and breakout labeling are all coherent |
| JLCPCB 2-layer manufacturability | **PASS with notes** — geometry inside process capability; 3 tight-but-legal items (see §5) |

The board is electrically correct against the v1 schematic, is fully manufactured-compatible geometry-wise, and is ready for JLCPCB fabrication. Three items are flagged as process-limit-tight or as informational; none are defects.

---

## 2. Evidence files

| Artifact | Path |
|---|---|
| DRC JSON (native CLI, all severities) | `.opencode/drc_cli23.json` |
| ERC JSON (native CLI, all severities) | `.opencode/erc-cli1.json` |
| Fresh netlist export from schematic | `.opencode/alcene-v1-fresh.nl` (54 KB, generated this session from `alcene-board-v1.kicad_sch`) |
| Parity comparator script | `.opencode/qcparse.py`, `.opencode/qcparse3.py` |

Nothing on the board was changed. No new files were added to the board or schematic.

---

## 3. DRC / ERC results

- **DRC** (native `kicad-cli`, `--severity-all`, schematic-parity field included in output): **0 violations, 0 unconnected items**.
- The DRC run's built-in *schematic-parity* check comes back empty because the board file stem (`...-rebased-zero-drc`) does not match the schematic file name, so KiCad cannot auto-link them on the CLI. This is why §4 performs the parity check manually instead — and the manual check is stricter anyway (pin-by-pin, not net-level only).
- **ERC:** 0 violations. The only ERC checks disabled are `single_global_label`, `four_way_junction`, `simulation_model_issue`, and `footprint_filter` — none of these affect electrical correctness of this design.
- The DRC run's *ignored checks* are benign too (`missing_courtyard`, `track_not_centered_on_via`, `tuning_profile_*`, `lib_footprint_mismatch`, footprint type/filter checks) — see §5.3 for the one that matters (courtyards).

---

## 4. Schematic ↔ PCB parity (manual, strict)

A post-merge netlist was freshly exported from the schematic **this session** and compared against the board, pad-by-pad, using net **partition membership** (not net names), because the net-name generation differs slightly between the two files for historical reasons (see §4.2).

### 4.1 Component parity

| Check | Result |
|---|---|
| Components on schematic | 14 (`J1 – J9`, `R1`, `R2`, `C1`, `C2`, `SW1`) |
| Components on board | 14 + `MH1`, `MH2` (2× NPTH mounting holes, no copper, no nets — mechanical only, legitimately absent from schematic) |
| `#FLG01` (PWR_FLAG) | schematic-only, virtual symbol, no footprint — correctly absent on board |
| Value mismatches | **0** |
| Footprint mismatches | **0** (first line of every footprint matches the netlist exactly) |
| Pad-level net mismatches | **0** of 145 schematic pins (board carries the matching 145 pads, plus 2 unnamed NPTH pads inside `MH1`/`MH2`) |
| Board pads with no schematic pin | **0** |
| Pads of `J2` marked *no-connect* on schematic (`A6`,`A7`,`A8`,`B6`,`B7`,`B8` = D+/D−/SBU pins) | correctly carry no copper net on board |

### 4.2 Net naming differences (cosmetic, connectivity identical)

Two nets carry different auto-generated names between the schematic and board while connecting **exactly** the same pad set (single source nets, renamed when the project was rebased):

| Schematic name | Board name | Membership |
|---|---|---|
| `Net-(J2-CC1)` | `Net-(J2-PadA5)` | J2 pin A5 + R1 pin 1 |
| `Net-(J2-CC2)` | `Net-(J2-PadB5)` | J2 pin B5 + R2 pin 1 |

All other 40 nets resolve under a standard `/` prefix difference only (`/VIN` ↔ `VIN` etc.). This is a KiCad auto-naming artifact, not a functional difference.

### 4.3 Full net map (schematic ↔ board equivalence, all 42 electrical nets)

Every net's pad membership matches exactly. Rail/intra-net membership summary:

- `GND` — 23 members: `J1.22`, `J3.1/21/22`, `J2.A1/A12/B1/B12/SH`, `J4.2`, `J7.1–8`, `R1.2`, `R2.2`, `SW1.1`, `C1.2`, `C2.2`
- `VIN` (= USB VBUS / 5 V rail) — 15 members: `J2.A4/A9/B4/B9`, `C1.1`, `C2.1`, `J1.21`, `J9.1–8`
- `3V3` — 12 members: `J1.1`, `J1.2`, `J4.1`, `J4.8`, `J8.1–8`
- `RST` — 2 members: `J1.3`, `SW1.2`
- `Net-(J2-PadA5)` / `Net-(J2-PadB5)` (CC1/CC2) — 2 members each: `J2.A5`+`R1.1` / `J2.B5`+`R2.1`
- GPIO nets — 2 members each (J1/J3 socket pin + matching J5/J6 breakout column pin), additionally `GPIO8`, `GPIO9`, `GPIO10`, `GPIO11`, `GPIO12`, `GPIO13` also reach `J4` (TFT) per the mapping in §4.4.
- `TX` — `J3.2` + `J6.1`; `RX` — `J3.3` + `J6.2`

### 4.4 TFT (`J4`) pin map — verified

Pin-by-pin (pads 1..14):

`3V3`, `GND`, `GPIO10`, `GPIO8`, `GPIO9`, `GPIO11`, `GPIO12`, `3V3`, `GPIO13`, `GPIO12`, `GPIO14`, `GPIO11`, `GPIO13`, `GPIO15`

This matches the standard 14-pin ILI9341 + resistive-touch module convention:

| J4 pin | Net | TFT function |
|---|---|---|
| 1 | 3V3 | VCC |
| 2 | GND | GND |
| 3 | GPIO10 | CS |
| 4 | GPIO8 | RESET |
| 5 | GPIO9 | DC/RS |
| 6 | GPIO11 | SDI/MOSI |
| 7 | GPIO12 | SCK |
| 8 | 3V3 | LED (backlight) |
| 9 | GPIO13 | SDO/MISO |
| 10 | GPIO12 | T_CLK (shared SPI clock) |
| 11 | GPIO14 | T_CS |
| 12 | GPIO11 | T_DIN (shared MOSI) |
| 13 | GPIO13 | T_DO (shared MISO) |
| 14 | GPIO15 | T_IRQ |

No strap-sensitive S3 pin is consumed by the display: `RST` TFT line is on `GPIO8` (not a boot strap on ESP32-S3; the strap pins are GPIO0/3/45/46). GPIO0, GPIO3, GPIO45 and GPIO46 appear **only** on the J5/J6 breakouts, never on a hard-wired device.

---

## 5. Electrical function review (board-level)

### 5.1 Power tree

```
USB-C J2 (GCT USB4085, 16-pin THT)  ──got VBUS─►  net VIN
    VIN ─┬─ C1 (10 µF, Murata GRM21BZ71E106KE15L, 0805, 25 V X7S)
         ├─ C2 (100 nF, Murata GRM21BR71H104KA01L, 0805, 50 V X7R)
         ├─ J1.21 (feeds ESP32-S3-DevKitC-1 "5V" pin → on-module regulator)
         └─ J9 (2×4 breakout, silks label "5V")

ESP32-S3 module ⇄ J1/J3 sockets:
    3V3 (module output) ─► J1.1, J1.2 ─┬─ J4.1/J4.8 (TFT VCC + LED)
                                       └─ J8 (2×4 breakout, silks "3V3")
```

- USB-C *power sink* (UFP) roles are correctly configured: **R1 = 5.1 kΩ** from CC1 (`J2.A5`) to GND and **R2 = 5.1 kΩ** from CC2 (`J2.B5`) to GND. Both pulldowns present → any USB-C source will detect the attach and deliver 5 V (spec-compliant default 5 V/3 A role). D+/D− and SBU pins are explicitly unconnected — i.e. the connector is used **for power only**, matching the design intent (data lives on the devkit's own USB-C).
- Decoupling placed at the connector: 10 µF bulk MLCC + 100 nF HF MLCC both on VIN/VBUS — correct and non-polarized, no polarity risk (they are MLCCs, not electrolytics).
- VIN enters the devkit at `J1.21`, consistent with the DevKitC-1 pin numbering (`5V` / right socket pin 21). Once the module boots, its 3 V3 output re-enters the board on `J1.1/J1.2`, feeding the TFT, its backlight, and the 3V3 breakout `J8`. There is no LDO on this PCB and it does not need one: all regulation happens on the module.
- Important behavior to keep in mind: **`VIN` and `3V3` are separate nets** with no component between them. Nothing on the board converts USB 5 V into 3.3 V - the ESP32 module does that. Correct.

### 5.2 Reset switch

`SW1 = SW_Push_SPST_NO_Alps_SKRK` (2 terminal pads used): pad 1 → `GND`, pad 2 → `RST`, `RST` also on `J1.3` (devkit EN). Pressing the button shorts `RST` to GND = clean hardware reset. The Alps SKRK's two terminals per side are internally bridged inside the button housing, so a 2-pad footprint configuration is functionally correct (a 2-pad SKRK footprints a standard dedup of the 4-pad variant with the redundant pads removed). **Works.**

### 5.3 ESP32-S3-DevKitC-1 socket mapping (`J1`, `J3`)

Board pads use 1×22-pin female strips at a 25.4 mm pitch, horizontally separated. Pin order and net assignment:

- `J1` (north→south): `3V3, 3V3, RST, GPIO4, GPIO5, GPIO6, GPIO7, GPIO15, GPIO16, GPIO17, GPIO18, GPIO8, GPIO3, GPIO46, GPIO9, GPIO10, GPIO11, GPIO12, GPIO13, GPIO14, VIN, GND`
- `J3` (north→south): `GND, TX, RX, GPIO1, GPIO2, GPIO42, GPIO41, GPIO40, GPIO39, GPIO38, GPIO37, GPIO36, GPIO35, GPIO0, GPIO45, GPIO48, GPIO47, GPIO21, GPIO20, GPIO19, GND, GND`

Both rows replicate the DevKitC-1 factory pin order exactly, and — critically — **pin 1 of both sockets sits at the same board end (north, y = 50 mm, pad 22 at y = 103.34 mm)**, which is what makes a non-mirrored module fit. That is the single most error-prone aspect of these boards, and it verifies correct here.

**Recommended (optional, cosmetic):** add a small USB/direction silk marker near J1/J3 so a future editor cannot insert the module 180° rotated. A wrong insertion would put 3V3 against a GND pin. Today the only hint is the GPIO silks labels next to `J5`/`J6`, not next to `J1`/`J3`.

### 5.4 GPIO breakouts (`J5`, `J6`)

Two distinct 18-pin single-row strips, 2.54 mm apart, mirroring the `J1` row (`J5`: GPIO19…GPIO14) and the `J3` row (`J6`: TX…GPIO20), excluding the pins already consumed by the rails, reset or the TFT. Each silk label sits next to the matching net. Verified: label ↔ net mapping is 1:1 correct.

---

## 6. JLCPCB manufacturability audit

### 6.1 Board geometry constraints vs. JLCPCB 2-layer capability

| Parameter | Board actual | JLCPCB capability (Std. 2-layer) | Verdict |
|---|---|---|---|
| Board size | **108.049 × 88.3 mm** | max 410 × 400 | ✅ Fabable, **but passes the 100 × 100 tier** → order will price at the "large board" tier instead of the ≤100×100 special; consider 2-up panelization only if you want the cheaper bracket |
| Copper layers | 2 (`F.Cu`, `B.Cu`, 197 + 132 track segments, 19 vias, **no zones**) | 2 | ✅ |
| Min track width | **0.2 mm** (0.2 / 0.3 / 0.5 used) | ≥ 0.127 | ✅ 1.57× margin |
| Min copper–copper clearance | ≥ 0.31 mm in tightest measured spot (CC1 B-lane vs `CC2` via) | ≥ 0.127 | ✅ |
| Copper–board edge | **rule fixed at 0.5 mm** in project and DRC enforces it | ≥ 0.3 | ✅ comfortably above fab min |
| Min drill (PTH) | **0.4 mm** (USB-C connector) | ≥ 0.3 | ✅ |
| Header PTH | 118 × Ø1.0 mm holes, Ø1.8–2.0 pads, annular 0.4–0.5 | fine | ✅ |
| Min via | **0.3 drill / 0.6 pad**, all 19 vias uniform | via drill ≥ 0.2, pad ≥ drill+0.3 | ✅ but exactly at the process limit (see §6.2) |
| NPTH | 2 × Ø3.0 mm mounting holes (MH1/MH2), no copper | min Ø0.8 NPTH | ✅ |
| Oval slots (USB-C shell) | 0.6 × (2.1 / 1.4) mm × 4 | min slot 0.6 | ✅ |
| Min annular ring, PTH signal pads | USB-C 0.4-hole / 0.7-pad → annular **0.15 mm** | ≥ 0.125–0.15 | ✅ exactly at process limit (see §6.2) |
| Solder-mask rules | default, vias tented front **and** back, no plugging/filling | — | ✅ |
| Silks text | 39 texts: min height **1.0 mm**, min stroke **0.15 mm** (three texts at 1.2 mm) | ≥ 0.8 mm / ≥ 0.15 mm | ✅ |

### 6.2 Items exactly at process limit — allowed, but zero margin

These are not defects, but they are the first things a marginal fab batch will trip on:

1. **19 bottom-layer vias at Ø0.3/Ø0.6 → annular ring exactly 0.150 mm.** JLC's published minimum is 0.3 mm hole + 0.3 mm added pad = 0.6 mm total = 0.15 mm ring. You pass with zero slack. Every extra µm of drill-bit wander keeps you inside the scratch-up bound. Nothing to fix today; on the next layout revision consider `Ø0.3/Ø0.65` for 0.175 ring.
2. **USB-C `Ø0.4` holes with `Ø0.7` pads** (16 pads) mean the same 0.15 mm annular. Same conclusion: passable, tight.

### 6.3 Notes that are not fab blockers

- **Several footprints have no courtyard outline** (USB-C J2, J1, J5, J7, J8, J9, C1, R2, MH1/MH2 among them). Because of that, the corresponding DRC check (`missing_courtyard`) is silenced in the project, which also means the *courtyard-overlap* DRC check never runs. For bare-PCB fabrication this is irrelevant. If you ever order JLC **SMT assembly (PCBA)**, the spacing between the R/C and any header is designer-verified, not rule-verified — double-check component spacing visually before ordering assembly, or backfill the courtyards.
- No copper pours/zones exist — everything is routed with discrete tracks. Fine for JLC.
- Board thickness/surface finish are **not encoded** in this file; pick them at order time (default 1.6 mm + HASL is what this layout's `pad_to_mask_clearance 0` setting assumes).
- The four `Edge.Cuts` lines are a simple rectangle, 108.049 × 88.3 mm, no notches / mouse bites / V-cut markers — single-board order, simplest case.

---

## 7. Summary of recommended (optional) improvements

1. **Add a north-arrow / USB-end silks marker** near `J1`-`J3` so the devkit cannot be inserted upside down.
2. **On the next revision only**, widen via pads from Ø0.6 to Ø0.65–0.7 for more annular margin (leave untouched as-is if this is a one-off).
3. **If PCBA is planned**, backfill the missing footprints' courtyards; not needed for bare-PCB orders.
4. `VIN` net is labeled `5V` on silks (under `J9`) — functionally correct and fine; just remember the net name is `VIN` in anything automated.

---

## 8. Conclusion

The board:

- is **electrically faithful** to `alcene-board-v1.kicad_sch` (component-by-component, pin-by-pin, value-by-value, footprint-by-footprint — verified mechanically in §4, not just trusted to DRC);
- is **functionally coherent** (power tree, USB-C sink role, reset, TFT SPI/touch mapping, breakouts);
- is **JLCPCB-fabricable as-is** (two boards available at account-wide min features, no blockers);
- and carries the standard post-layout artifacts you would expect from a completed design: 0 DRC errors, 0 DRC warnings, 0 ERC errors, 0 unconnected nets, 0 parity differences.

No changes were made to the board during this QC pass.
