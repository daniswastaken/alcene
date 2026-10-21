# alcene-board-v1 Final PCB Quality Assurance Report

## A. Project identity

- Authoritative schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- Original PCB: `X:\alcene\kicad\alcene-board-v1-connectivity-verified.kicad_pcb`
- Working/final PCB: `X:\alcene\kicad\alcene-board-v1-final-qc.kicad_pcb`
- Backup PCB: `X:\alcene\kicad\alcene-board-v1-pre-final-qc-backup.kicad_pcb`
- KiCad backend: SWIG, realtime IPC not connected
- Copper layers: `F.Cu`, `B.Cu` only (2 copper layers)
- Board outline: closed 107.1 mm x 87.1 mm rectangle (`Edge.Cuts`)
- Schematic ERC: 0 errors, 0 warnings, 0 info

## B. Electrical verification

- Schematic components: 14 board components plus `#FLG01` power flag and mounting holes `MH1`, `MH2` on PCB only.
- PCB components: 17 placed footprints including `MH1`, `MH2`.
- Component reference and footprint correspondence: PASS for all schematic components.
- Pad-to-net comparison: PASS for all 14 schematic components. Net assignments on PCB match fresh schematic netlist.
- GND: PASS. All 26 expected GND pads are assigned to `GND`; zone refill completed on `B.Cu`.
- 3V3: PASS. All 12 expected 3V3 pads assigned to `3V3`.
- VIN/USB-C: PASS. `J2` VBUS pads A4, A9, B4, B9 are assigned to `VIN`; C1 and C2 pin 1 are `VIN`; J1 pin 21 and J9 pins 1-8 are `VIN`.
- CC1/CC2: PASS. `J2 A5` -> `Net-(J2-PadA5)` -> R1 pin 1; `J2 B5` -> `Net-(J2-PadB5)` -> R2 pin 1; R1/R2 pin 2 -> `GND`.
- Reset: PASS. `J1` pin 3 (`RST`) connected to `SW1` pin 2; `SW1` pin 1 -> `GND`.
- GPIO breakouts: PASS. J5 and J6 mappings match fresh netlist; J6 omits GPIO19 as intended.
- TFT connector: PASS. All 14 J4 pads match the approved mapping and schematic netlist.

## C. PCB integrity

- Initial/final unrouted count: DRC reports no `unconnected_items`; ratsnest generated for all 42 nets with routed segments. No missing required connection identified.
- Initial DRC: 43 violations (33 errors, 10 warnings).
- Final DRC after zone refill: 43 violations (33 errors, 10 warnings).
- Tracks: 362 track segments; vias present where layer transitions are required.
- Copper zones: 1 GND zone on `B.Cu`, refilled successfully.
- Shorts: none identified by DRC.
- Board outline: valid closed rectangle on `Edge.Cuts`.
- Footprint compatibility: standard KiCad footprints used; 2 `lib_footprint_mismatch` warnings for `MountingHole_3mm` only.

## D. Manufacturing readiness

- Silkscreen: present on both sides; 8 `silk_overlap` warnings remain.
- 3D models: present for USB-C, ESP32 sockets, GPIO headers, power headers, TFT socket, reset switch, R1, R2, C1, C2. Mounting holes have no 3D model.
- Drill files: PTH and NPTH Excellon files plus PDF maps generated.
- Gerber files: F.Cu, B.Cu, F.Mask, B.Mask, F.Silkscreen, B.Silkscreen, Edge.Cuts plus job file generated.
- Manufacturer-specific rules: not confirmed. Generic fabrication package provided.

## E. Change record

- No PCB component positions, rotations, board outline, silkscreen, footprint identities, copper-layer configuration, or schematic were changed.
- Zone refill executed on the final working copy.
- No copper tracks or vias were added, deleted, or moved.
- No DRC rules were disabled or relaxed.

## F. Remaining risks

1. Severity: Medium. Evidence: 30 `clearance` DRC errors, including 0.15 mm actual between adjacent USB-C pads and 0.15 mm actual between R1/R2 and C1/C2 pads. Consequence: may challenge fabrication or assembly depending on manufacturer capability. Blocks fabrication: No for generic prototype if manufacturer accepts 0.15 mm; Yes if strict 0.2 mm rule is enforced. Recommended action: confirm manufacturer minimum clearance or slightly increase component spacing in a future revision.
2. Severity: Low. Evidence: 3 `courtyards_overlap` DRC errors at R1/R2, C1/C2, and J5/J6. Consequence: reduced assembly clearance. Blocks fabrication: No. Recommended action: owner decision on dense placement; no electrical impact.
3. Severity: Low. Evidence: 8 `silk_overlap` warnings. Consequence: silkscreen legibility may suffer. Blocks fabrication: No. Recommended action: minor text movement if desired.
4. Severity: Low. Evidence: 2 `lib_footprint_mismatch` warnings for mounting holes. Consequence: library copy differs from board copy. Blocks fabrication: No. Recommended action: update footprint library or ignore.
5. Severity: Medium. Evidence: no physical fit test performed. Consequence: connector/header/USB-C mechanical fit unverified. Blocks fabrication: No, but prototype validation required. Recommended action: build and inspect first article.
6. Severity: Low. Evidence: capacitor DC-bias derating not quantified. Consequence: effective capacitance under bias may be lower than nominal. Blocks fabrication: No. Recommended action: review manufacturer curves if capacitance tolerance is critical.

## Final release verdict

CONDITIONALLY APPROVED
