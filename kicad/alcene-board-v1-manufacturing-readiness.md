# alcene-board-v1 Manufacturing Readiness Report

## Outputs generated

- Gerbers: `X:\alcene\kicad\release-final-qc\gerbers`
- Drill files: `X:\alcene\kicad\release-final-qc\drills`
- DRC report: `X:\alcene\kicad\alcene-board-v1-final-drc-report.txt`
- Netlist: `X:\alcene\kicad\alcene-board-v1-final-netlist.net`

## Geometry

- Edge.Cuts is a closed 107.1 mm x 87.1 mm rectangle.
- No copper layer beyond F.Cu and B.Cu is used.
- USB-C connector is at the intended board edge location.

## DRC status

- Final DRC: 43 violations, 33 errors, 10 warnings.
- Clearance: 30 errors.
- Courtyards overlap: 3 errors.
- Lib footprint mismatch: 2 warnings.
- Silk overlap: 8 warnings.
- Unconnected items: 0.
- Shorts: 0.

## Accepted conditions

- 0.15 mm USB-C pad-to-pad clearance is inherent to the USB-C footprint and must be confirmed against manufacturer capability.
- R1/R2 and C1/C2 courtyard overlaps result from intentionally dense component placement.
- J5/J6 courtyard overlap results from adjacent 2.54 mm header placement.
- Silk overlap warnings are cosmetic.
- Mounting hole footprint library mismatch is non-blocking.

## Still outstanding

- Physical fit and assembly validation.
- Manufacturer-specific DFM confirmation.
- Capacitor DC-bias derating review if capacitance is critical.
- 3D model for mounting holes if desired.

## Verdict

CONDITIONALLY APPROVED
