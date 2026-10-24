# Final Connectivity Report

Corrected board: `X:\alcene\kicad\alcene-board-v1-j4-corrected.kicad_pcb`

Backup: `X:\alcene\kicad\alcene-board-v1-before-j4-flip-backup.kicad_pcb`

J4 is rotated 180 degrees in plane. Pad 1/3V3 is leftmost and pad 14/GPIO15 is rightmost. All 14 J4 pads match the schematic net assignments.

Affected TFT/touch nets were rerouted and connected to their ESP32 and GPIO breakout endpoints. Shared nets GPIO11, GPIO12, and GPIO13 retain both TFT/touch functions.

USB-C power, CC, ground, 3V3, reset, and power header architecture were preserved. J2 was not moved. Board outline and non-J4 footprint positions were preserved. Only F.Cu and B.Cu are used.

ERC: 0 violations. DRC: 121 violations, none are shorts or dangling tracks. Final unrouted count: 0.