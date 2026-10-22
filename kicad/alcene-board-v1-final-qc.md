# alcene-board-v1 Final PCB Quality Assurance Report

## A. Project identity

- Authoritative schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- Final PCB: `X:\alcene\kicad\alcene-board-v1-final-release.kicad_pcb`
- Backup PCB: `X:\alcene\kicad\alcene-board-v1-pre-final-release-backup.kicad_pcb`
- KiCad backend: SWIG, realtime IPC not connected
- Copper layers: `F.Cu`, `B.Cu` only (2 copper layers)
- Board outline: closed 107.1 mm x 87.1 mm rectangle (`Edge.Cuts`)
- Schematic ERC: 0 errors, 0 warnings, 0 info

## B. Electrical verification

- Schematic components: 14 board components plus power flag `#FLG01`; mounting holes `MH1`, `MH2` are PCB-only.
- PCB components: 17 placed footprints.
- Component reference and footprint correspondence: PASS for all schematic components.
- Pad-to-net comparison: PASS for all 14 schematic components.
- GND: PASS. All 26 expected GND pads assigned to `GND`; B.Cu GND zone refilled.
- 3V3: PASS. All 12 expected 3V3 pads assigned to `3V3`.
- VIN/USB-C: PASS. J2 VBUS pads A4, A9, B4, B9 are `VIN`; C1/C2 pin 1 are `VIN`; J1 pin 21 and J9 pins 1-8 are `VIN`.
- CC1/CC2: PASS. J2 A5 -> R1 pin 1 -> R1 pin 2 -> GND; J2 B5 -> R2 pin 1 -> R2 pin 2 -> GND.
- Reset: PASS. J1 pin 3 (`RST`) -> SW1 pin 2; SW1 pin 1 -> GND.
- GPIO breakouts: PASS. J5/J6 mappings match fresh netlist; J6 omits GPIO19 as intended.
- TFT connector: PASS. All 14 J4 pads match approved mapping and schematic netlist.

## C. PCB integrity

- Unrouted count: 0; DRC reports no `unconnected_items`.
- DRC final: 40 violations (32 errors, 8 warnings).
  - 29 clearance errors: 0.15 mm USB-C or resistor pad-to-pad, within JLCPCB 0.15 mm minimum.
  - 3 courtyard-overlap errors: conservative or intentional dense placement.
  - 8 silkscreen-overlap warnings: cosmetic.
- Tracks: 362 track segments plus 4 corrected segments; required vias present.
- Copper zones: 1 GND zone on `B.Cu`, refilled successfully.
- Shorts: none identified by DRC.
- Board outline: valid closed rectangle on `Edge.Cuts`.
- Footprint mismatch: resolved by replacing both `MountingHole_3mm` footprints with library copies at original positions.

## D. Changes made

- C2 moved 0.20 mm right to correct a 0.10 mm C1/C2 pad-to-pad clearance.
- Four local track segments rerouted to preserve C2 connectivity.
- MH1 and MH2 replaced with library `MountingHole:MountingHole_3mm` at original positions and rotations.
- Header value text hidden on J5, J6, and J7 to reduce silkscreen clutter.
- Zone refill executed on final working copy.
- No schematic, power architecture, component values, or GPIO mappings changed.

## E. Manufacturing readiness

- Silkscreen: present on both sides; GPIO labels preserved.
- 3D models: present for USB-C, ESP32 sockets, GPIO headers, power headers, TFT socket, reset switch, R1, R2, C1, C2.
- Drill files: PTH and NPTH Excellon files plus PDF maps generated.
- Gerber files: F.Cu, B.Cu, F.Mask, B.Mask, F.Silkscreen, B.Silkscreen, Edge.Cuts plus job file generated.
- Finish: black solder mask, white silkscreen, 2-layer FR-4, 1 oz outer copper.
- Physical connector and display fit: not physically tested; prototype validation required.
- Capacitor DC-bias derating: not quantified; review manufacturer data if capacitance is critical.

## F. Final release verdict

CONDITIONALLY READY — specific documented exceptions
