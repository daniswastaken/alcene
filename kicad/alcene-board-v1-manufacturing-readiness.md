# alcene-board-v1 Manufacturing Readiness Report

## Outputs generated

- Gerbers: `X:\alcene\kicad\release-candidate-final\gerbers`
- Drill files: `X:\alcene\kicad\release-candidate-final\drills`
- DRC report: `X:\alcene\kicad\alcene-board-v1-final-drc-report.txt`
- Netlist: `X:\alcene\kicad\alcene-board-v1-final-netlist.net`
- Clearance exceptions: `X:\alcene\kicad\alcene-board-v1-clearance-exceptions.md`

## Geometry

- Edge.Cuts is a closed 107.1 mm x 87.1 mm rectangle.
- Only F.Cu and B.Cu are used.
- USB-C connector remains at the intended board edge.

## DRC status

- Final DRC: 40 violations, 32 errors, 8 warnings.
- Clearance: 29 errors, all 0.15 mm SMD-pad-to-SMD-pad and within JLCPCB 2-layer 1 oz minimum of 0.15 mm.
- Courtyards overlap: 3 errors, conservative or intentional dense placement.
- Silk overlap: 8 warnings, cosmetic.
- Unconnected items: 0.
- Shorts: 0.

## Electrical status

- ERC: 0 errors, 0 warnings, 0 info.
- All required power, ground, CC, reset, GPIO, and TFT connections match schematic.
- Direct VBUS-to-VIN architecture preserved.

## Accepted conditions

- 0.15 mm USB-C and resistor pad clearances are acceptable under JLCPCB standard 2-layer 1 oz capability.
- R1/R2 and C1/C2 courtyard overlaps are conservative, with no body collision.
- J5/J6 courtyard overlap is intentional dense header placement.
- Remaining silkscreen warnings are cosmetic.
- Physical fit and capacitor DC-bias derating remain unverified.

## Finish

- Black solder mask.
- White silkscreen.
- 2-layer FR-4.
- 1 oz outer copper.

## Verdict

CONDITIONALLY READY — specific documented exceptions
