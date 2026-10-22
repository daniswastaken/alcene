# alcene-board-v1 Clearance Exception Report

## Manufacturing assumption

- Manufacturer: JLCPCB
- Process: standard FR-4, 2 layers, 1 oz finished outer copper
- Published minimum track spacing: 0.10 mm
- Published different-net SMD pad-to-pad spacing: 0.15 mm

## Clearance violations

| ID | Type | Objects/references | Actual | Project rule | JLCPCB minimum | Genuine defect? | Disposition |
|---|---|---|---:|---:|---:|---|---|
| C1 | SMD pad to SMD pad | C1 pad 2 (`GND`) to C2 pad 1 (`VIN`) | 0.10 mm | 0.20 mm | 0.15 mm | Yes | Corrected by moving C2 0.20 mm right; new clearance 0.30 mm |
| USB1-USB28 | SMD pad to SMD pad | Adjacent USB-C receptacle pads on different nets | 0.15 mm | 0.20 mm | 0.15 mm | No | Accepted: meets published 0.15 mm minimum |
| R1-R2 | SMD pad to SMD pad | R1 pad 2 (`GND`) to R2 pad 1 (`Net-(J2-PadB5)`) | 0.15 mm | 0.20 mm | 0.15 mm | No | Accepted: meets published 0.15 mm minimum |

## Notes

- All 29 remaining clearance errors are 0.15 mm USB-C or resistor pad-to-pad clearances.
- No pad-to-track, track-to-track, via, through-hole, or copper-to-edge clearance violation remains.
- No DRC rule was globally weakened.
- The C1/C2 clearance was corrected with a minimal 0.20 mm footprint movement and local track reroute.
- Fresh DRC on final PCB: 40 violations, 32 errors, 8 warnings.
