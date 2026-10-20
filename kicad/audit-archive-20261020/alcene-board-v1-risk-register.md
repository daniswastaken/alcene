# alcene-board-v1 Risk Register

| ID | Component / net | Observed condition | Expected behavior | Failure mode | Severity | Status | Blocks layout? | Blocks prototype? | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| R1 | D1 / VIN | D1 is absent; J2 VBUS is wired directly to VIN | SS14 between J2 VBUS and VIN, anode to VBUS, cathode to VIN | No reverse-current protection; USB port can be backfed from VIN/J9 | High | FAIL | Yes | Yes | Component inventory, netlist, backup schematic |
| R2 | J9 / VIN | J9 is wired to VIN with no isolation or source control | Distribution header only | External supply on J9 can energize VIN and backfeed USB if D1 absent | High | FAIL | Yes | Yes | Netlist, schematic wiring |
| R3 | J2 USB-C | Two 5.1 kohm CC pull-downs only | Basic Type-C sink | Source current above default 500 mA is not detected or negotiated | Medium | CONDITIONAL PASS | No | No | J2 symbol, resistor values, USB-C spec |
| R4 | VIN / AMS1117 | Intended SS14 VF reduces VIN margin | Stable 3.3 V regulation | Regulator dropout during low VBUS or high current | Medium | CONDITIONAL PASS | No | Yes | Datasheet VF max 0.5 V, LDO dropout estimate |
| R5 | C1 / C2 | No voltage rating or dielectric recorded | Adequate rating for 5 V USB environment | Derating or dielectric failure if parts are underrated | Medium | UNVERIFIED | No | Yes | Component properties |
| R6 | J4 pin 8 / 3V3 | Backlight tied directly to 3V3, no series resistor | Controlled backlight current | Excess backlight current if module lacks onboard limiting | Medium | UNVERIFIED | No | Yes | Netlist, schematic |
| R7 | J4 TFT | Exact module not identified in project files | Verified module pinout and VCC | Pinout or voltage mismatch if module differs | Medium | UNVERIFIED | No | Yes | Component value only |
| R8 | J1/J3 | Pin mapping matches official DevKit table | Correct DevKit fit | Wrong GPIO usage if variant differs | Low | PASS | No | No | Official Espressif table |
| R9 | J5/J6 | GPIO19 moved to J5; J6 omits it | Intended breakout mapping | Header silkscreen/documentation mismatch | Low | PASS | No | No | Netlist |
| R10 | J7/J8/J9 | All pins tied to one net each | Intended distribution headers | Accidental power injection if used as input | Medium | PASS with restriction | No | No | Netlist |
| R11 | 3V3 rail | No isolation between DevKit regulator and external 3V3 | Single source or documented restriction | Backpowering regulator | Medium | CONDITIONAL PASS | No | No | DevKit documentation |
| R12 | SW1 | Wires cross J1 symbol body | Clean schematic routing | ERC passes; documentation/cosmetic issue | Low | PASS | No | No | find_wires_crossing_symbols |
| R13 | ERC | 0 errors, 9 multiple_net_names warnings | Clean net names | Ambiguous documentation | Low | PASS | No | No | erc-fresh.json |
| R14 | J2 shield | Shield tied directly to GND | Intentional shield grounding | Ground loop or ESD policy may need review | Low | CONDITIONAL PASS | No | No | Netlist |
| R15 | C1/C2 placement | Upstream of intended diode | Input decoupling | Less downstream decoupling after diode | Low | CONDITIONAL PASS | No | No | Netlist |

## Severity guide

- High: concrete defect or safety/contention issue that blocks layout or prototype.
- Medium: must be resolved or explicitly accepted before prototype fabrication.
- Low: documentation, cosmetic, or prototype-validation item.

## Priority plan

### Priority 1 - before PCB layout

1. Restore or explicitly remove D1. If restored, use `Device:D_Schottky`, SS14, footprint `Diode_SMD:D_SMA`, anode to J2 VBUS, cathode to VIN.
2. Resolve J9 power injection policy. Either add hardware isolation or document and enforce single-source operation.
3. Decide whether 3V3 can be externally driven. If not, mark J8/J1 3V3 as outputs only.

### Priority 2 - before prototype fabrication

1. Obtain C1/C2 voltage rating and dielectric.
2. Verify TFT module backlight current limiting or add a calculated series resistor.
3. Confirm USB source current capability and maximum load.
4. Measure regulator dropout margin with the intended diode.

### Priority 3 - documentation and usability

1. Clean multiple-net-name aliases.
2. Correct J5 description if it is not purely J1 signals.
3. Reroute wires that cross J1.
4. Add design notes for boot-strapping and USB pins.