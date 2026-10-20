# alcene-board-v1 Risk Register — Final Revision

| ID | Component / net | Observed condition | Expected / accepted behavior | Failure mode | Severity | Status | Blocks schematic sign-off? | Blocks PCB layout? | Blocks prototype? |
|---|---|---|---|---|---|---|---|---|---|
| R1 | D1 / VIN | D1 intentionally absent; J2 VBUS directly connected to VIN | Direct VBUS architecture selected by owner | No reverse-current blocking between VIN and J2 VBUS | Medium | ACCEPTED BY OWNER | No | No | No |
| R2 | J9 / VIN | J9 wired to VIN with no isolation | Distribution output only | External injection if misused | Medium | ACCEPTED BY OWNER | No | No | No |
| R3 | J8 / 3V3 | J8 wired to 3V3 with no isolation | Distribution output only | External injection if misused | Medium | ACCEPTED BY OWNER | No | No | No |
| R4 | J2 USB-C | Two 5.1 kohm CC pull-downs only | Basic USB Type-C sink | Source current above default is not detected | Medium | CONDITIONAL PASS | No | No | No |
| R5 | VIN / regulator | Direct VBUS improves margin over SS14 path | Stable 3.3 V regulation | Dropout under low source voltage or high load | Medium | CONDITIONAL PASS | No | Yes | Yes |
| R6 | C1 / C2 | Voltage rating and dielectric now specified | 25 V and 50 V X7R parts selected | C1 DC-bias derating may reduce effective capacitance | Low | CONDITIONAL PASS | No | No | Yes |
| R7 | J4 TFT | Owner-confirmed pinout and direct 3V3 backlight | Preserve exact mapping | Incorrect only if owner's confirmation is wrong | Medium | ACCEPTED BY OWNER | No | No | No |
| R8 | J4 pin 8 | Backlight tied directly to 3V3 | Owner-confirmed direct connection | Backlight current depends on module | Medium | ACCEPTED BY OWNER | No | No | No |
| R9 | J1/J3 | Pin mapping matches official DevKit table | Correct DevKit fit | Variant-dependent GPIO restrictions | Low | PASS | No | No | No |
| R10 | J5/J6 | GPIO19 moved to J5; J6 omits it | Intended breakout mapping | Documentation mismatch only | Low | PASS | No | No | No |
| R11 | J7/J8/J9 | All pins tied to one net each | Intended distribution headers | Accidental power injection if misused | Low | PASS with restriction | No | No | No |
| R12 | 3V3 rail | No isolation between regulator and external 3V3 | Single source or documented restriction | Regulator backpowering if misused | Medium | CONDITIONAL PASS | No | No | No |
| R13 | SW1 | Reset switch wires rerouted | Clean schematic routing | None after cleanup | Low | PASS | No | No | No |
| R14 | ERC | 0 errors, 0 warnings | Clean report | None | Low | PASS | No | No | No |
| R15 | J2 shield | Shield tied directly to GND | Intentional shield grounding | Grounding policy may need review | Low | CONDITIONAL PASS | No | No | No |
| R16 | Physical fit | Connector dimensions not verified | Confirm before fabrication | Mechanical interference | Medium | UNVERIFIED | No | No | Yes |

Status labels:
- PASS: verified.
- FAIL: concrete defect.
- UNVERIFIED: required evidence missing.
- CONDITIONAL PASS: acceptable under stated conditions.
- ACCEPTED BY OWNER: owner-confirmed design choice.

No item currently blocks schematic sign-off or PCB layout. Prototype-only items remain for C1 DC-bias verification, backlight current, and physical fit.