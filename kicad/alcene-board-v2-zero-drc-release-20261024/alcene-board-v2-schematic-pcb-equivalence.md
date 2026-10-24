# Schematic <-> PCB equivalence - alcene-board-v2 (rebase, zero-DRC)

Date: 2026-10-24

## Inputs

- Authority schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch` (sha256 `08026ec81014bcb09f79c1263d349cc3a4ec7caec9ffadf2b03eb270e60afa0d`), ERC 0/0.
- Board: `X:\alcene\kicad\alcene-board-v2-rebased-zero-drc.kicad_pcb` (the shipped file).
- Netlist: exported from the schematic via KiCad into this release dir
  (`alcene-board-v2-netlist.net`), node-level (ref, pin) per net.

## Method

Pad-net map parsed from the shipped board file (each embedded footprint
pad -> `(net "NAME")`), node map parsed from the exported schematic
netlist.  Sets compared **net-by-net**: a net matches iff its
`{(ref, pad)}` set is identical.  Pure net *renames* (schematic-internal
auto names vs board names) are reported as a mapping table, not diffs.

## Result

- Schematic nets: 48, nodes: 145
- Board named nets: 42, netted pads: 139
- Nets identical by node-set: **48 / 48**
- Unmatched nets (bi-directional): **none**

| `/3V3` | 12 | `3V3` | renamed -> see mapping |
| `/GND` | 23 | `GND` | renamed -> see mapping |
| `/GPIO0` | 2 | `GPIO0` | renamed -> see mapping |
| `/GPIO1` | 2 | `GPIO1` | renamed -> see mapping |
| `/GPIO2` | 2 | `GPIO2` | renamed -> see mapping |
| `/GPIO3` | 2 | `GPIO3` | renamed -> see mapping |
| `/GPIO4` | 2 | `GPIO4` | renamed -> see mapping |
| `/GPIO5` | 2 | `GPIO5` | renamed -> see mapping |
| `/GPIO6` | 2 | `GPIO6` | renamed -> see mapping |
| `/GPIO7` | 2 | `GPIO7` | renamed -> see mapping |
| `/GPIO8` | 3 | `GPIO8` | renamed -> see mapping |
| `/GPIO9` | 3 | `GPIO9` | renamed -> see mapping |
| `/GPIO10` | 3 | `GPIO10` | renamed -> see mapping |
| `/GPIO11` | 4 | `GPIO11` | renamed -> see mapping |
| `/GPIO12` | 4 | `GPIO12` | renamed -> see mapping |
| `/GPIO13` | 4 | `GPIO13` | renamed -> see mapping |
| `/GPIO14` | 3 | `GPIO14` | renamed -> see mapping |
| `/GPIO15` | 3 | `GPIO15` | renamed -> see mapping |
| `/GPIO16` | 2 | `GPIO16` | renamed -> see mapping |
| `/GPIO17` | 2 | `GPIO17` | renamed -> see mapping |
| `/GPIO18` | 2 | `GPIO18` | renamed -> see mapping |
| `/GPIO19` | 2 | `GPIO19` | renamed -> see mapping |
| `/GPIO20` | 2 | `GPIO20` | renamed -> see mapping |
| `/GPIO21` | 2 | `GPIO21` | renamed -> see mapping |
| `/GPIO35` | 2 | `GPIO35` | renamed -> see mapping |
| `/GPIO36` | 2 | `GPIO36` | renamed -> see mapping |
| `/GPIO37` | 2 | `GPIO37` | renamed -> see mapping |
| `/GPIO38` | 2 | `GPIO38` | renamed -> see mapping |
| `/GPIO39` | 2 | `GPIO39` | renamed -> see mapping |
| `/GPIO40` | 2 | `GPIO40` | renamed -> see mapping |
| `/GPIO41` | 2 | `GPIO41` | renamed -> see mapping |
| `/GPIO42` | 2 | `GPIO42` | renamed -> see mapping |
| `/GPIO45` | 2 | `GPIO45` | renamed -> see mapping |
| `/GPIO46` | 2 | `GPIO46` | renamed -> see mapping |
| `/GPIO47` | 2 | `GPIO47` | renamed -> see mapping |
| `/GPIO48` | 2 | `GPIO48` | renamed -> see mapping |
| `/RST` | 2 | `RST` | renamed -> see mapping |
| `/RX` | 2 | `RX` | renamed -> see mapping |
| `/TX` | 2 | `TX` | renamed -> see mapping |
| `/VIN` | 15 | `VIN` | renamed -> see mapping |
| `Net-(J2-CC1)` | 2 | `Net-(J2-PadA5)` | renamed -> see mapping |
| `Net-(J2-CC2)` | 2 | `Net-(J2-PadB5)` | renamed -> see mapping |
| `unconnected-(J2-D+-PadA6)` | 1 | `None` | unconnected symbol pin (board: netless pad) |
| `unconnected-(J2-D+-PadB6)` | 1 | `None` | unconnected symbol pin (board: netless pad) |
| `unconnected-(J2-D--PadA7)` | 1 | `None` | unconnected symbol pin (board: netless pad) |
| `unconnected-(J2-D--PadB7)` | 1 | `None` | unconnected symbol pin (board: netless pad) |
| `unconnected-(J2-SBU1-PadA8)` | 1 | `None` | unconnected symbol pin (board: netless pad) |
| `unconnected-(J2-SBU2-PadB8)` | 1 | `None` | unconnected symbol pin (board: netless pad) |
## Name mapping (auto rename only)

| `/3V3` | `3V3` |
| `/GND` | `GND` |
| `/GPIO0` | `GPIO0` |
| `/GPIO1` | `GPIO1` |
| `/GPIO2` | `GPIO2` |
| `/GPIO3` | `GPIO3` |
| `/GPIO4` | `GPIO4` |
| `/GPIO5` | `GPIO5` |
| `/GPIO6` | `GPIO6` |
| `/GPIO7` | `GPIO7` |
| `/GPIO8` | `GPIO8` |
| `/GPIO9` | `GPIO9` |
| `/GPIO10` | `GPIO10` |
| `/GPIO11` | `GPIO11` |
| `/GPIO12` | `GPIO12` |
| `/GPIO13` | `GPIO13` |
| `/GPIO14` | `GPIO14` |
| `/GPIO15` | `GPIO15` |
| `/GPIO16` | `GPIO16` |
| `/GPIO17` | `GPIO17` |
| `/GPIO18` | `GPIO18` |
| `/GPIO19` | `GPIO19` |
| `/GPIO20` | `GPIO20` |
| `/GPIO21` | `GPIO21` |
| `/GPIO35` | `GPIO35` |
| `/GPIO36` | `GPIO36` |
| `/GPIO37` | `GPIO37` |
| `/GPIO38` | `GPIO38` |
| `/GPIO39` | `GPIO39` |
| `/GPIO40` | `GPIO40` |
| `/GPIO41` | `GPIO41` |
| `/GPIO42` | `GPIO42` |
| `/GPIO45` | `GPIO45` |
| `/GPIO46` | `GPIO46` |
| `/GPIO47` | `GPIO47` |
| `/GPIO48` | `GPIO48` |
| `/RST` | `RST` |
| `/RX` | `RX` |
| `/TX` | `TX` |
| `/VIN` | `VIN` |
| `Net-(J2-CC1)` | `Net-(J2-PadA5)` |
| `Net-(J2-CC2)` | `Net-(J2-PadB5)` |
## The blank net

The board file carries netcode 0 with an empty name.  This is KiCad's
default "unconnected" net bucket; it owns **no pads** on this board
(mounting holes MH1/MH2 are deliberately netless).  It is benign, cannot
carry copper, and is not a schematic item.
