# alcene-board-v1 PCB Layout Report — Revision R3

- PCB: `X:\alcene\kicad\alcene-board-v1-layout-r3.kicad_pcb`
- Backup: `X:\alcene\kicad\alcene-board-v1-layout-r2-before-refinement-backup.kicad_pcb`
- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- KiCad version: 10.0.7
- Date: 2026-10-20
- Layers: F.Cu and B.Cu only

## Placement

- J2 USB-C is locked and unchanged: X=41.525 mm, Y=109.966 mm, rotation=0°, footprint `Connector_USB:USB_C_Receptacle_GCT_USB4085`.
- J5/J6 remain a tightly paired 2-column x 18-row GPIO breakout assembly.
- J1/J3 remain parallel ESP32-S3 socket rows.
- J8, J7, and J9 remain horizontal 4x2 power headers in 3V3, GND, VIN order.
- J4 remains horizontal along the TFT reservation.
- The TFT display-area indicator and `2.8 INCH TFT DISPLAY AREA` label remain on F.Silkscreen.
- Minor alignment adjustments were made to power headers, ESP32 sockets, GPIO rows, and power-entry passives.
- Board outline resized to 160 mm x 130 mm to contain the existing component envelope.

## Routing

- Obsolete traces were removed and the board was rerouted with Freerouting.
- Tracks: 370.
- Vias: 5.
- B.Cu GND copper pour retained.
- 52 narrow traces were widened to 0.2 mm.

## DRC

- Total violations: 71
- Errors: 33
- Warnings: 38
- Clearance: 30
- Courtyards overlap: 3
- Silkscreen overlap: 37
- Via dangling: 1
- Track width: 0

## 3D models

- Attempted to attach standard KiCad 3D models to R1, R2, C1, C2, J1, J3, J5, J6, J7, J8, J9, J4, J2, and SW1.
- Attachment failed because the live IPC backend is unavailable in this environment.
- No 3D model coverage change was made.
- A 3D model audit report is not complete; model coverage remains unverified.

## Status

Routing and placement refinement are complete, but the board is not DRC-clean and 3D model coverage was not completed. It is not approved for prototype fabrication. J2 remained exactly unchanged. No schematic electrical changes were made.