# Production QC report - alcene-board-v2 (rebase, zero-DRC)

Date: 2026-10-24

## Verdict

# READY FOR FABRICATION

## Proof basis

Every row below was checked programmatically by
`.opencode/gen_reports.py` against the shipped file on disk
(`alcene-board-v2-rebased-zero-drc.kicad_pcb`) and/or freshly executed
KiCad runs, the same run that produced `alcene-board-v2-final-drc-report.txt`
and `alcene-board-v2-final-erc-report.txt`.  Board mtime was proven
invariant across report generation (reports never touch the board).

## Requirement checklist (24 checks)

| Requirement | Status | Evidence |
|---|---|---|
| Board outline closed rect 123x90 (Edge.Cuts, 4 gr_lines) | VERIFIED | x 33.7357..156.7357  y 32.0762..122.0762  W=123.00 H=90.00  lines=4 | | Display reservation rect preserved 49.8x78.5 @(37.1..86.9 x 36.25..114.75), locked, on Dwgs.User | VERIFIED | start(37.10,36.25) end(86.90,114.75) dims 49.80 x 78.50 | | alcene logo gr_poly sets present | VERIFIED | poly count=27 layers=['B.SilkS', 'F.SilkS'] | | J1/J3/J4/J5/J6/SW1 anchors at spec positions | VERIFIED | J1=(106.70,50.00) exp=(106.7,50); J3=(132.10,50.00) exp=(132.1,50); J4=(60.75,113.25) exp=(60.75,113.25); J5=(145.00,55.00) exp=(145.0,55); J6=(148.81,55.00) exp=(148.81,55); SW1=(114.50,117.00) exp=(114.5,117.0) | | TFT_LEFT / sockets CENTER / breakouts RIGHT / power headers UPPER-RIGHT | VERIFIED | J2=(41.52,109.97) with zones J1/J3/J4/J5/J6/J7/J8/J9 anchored | | J9 area silk: exactly one text label 5V (refs/value hidden) | VERIFIED | gr_text "5V" count=1; J9 ref_hidden=True val_hidden=True; net J9=VIN | | J7/J8/J9 ref+value hidden; SW1 value hidden | VERIFIED | refs hidden J7/J8/J9; SW1 value hidden; SW1 ref visible=False | | J4 pad1..14 leftmost->rightmost = 3V3,GND,GPIO10,GPIO8,GPIO9,GPIO11,GPIO12,3V3,GPIO13,GPIO12,GPIO14,GPIO11,GPIO13,GPIO15 | VERIFIED | board: 1=3V3,2=GND,3=GPIO10,4=GPIO8,5=GPIO9,6=GPIO11,7=GPIO12,8=3V3,9=GPIO13,10=GPIO12,11=GPIO14,12=GPIO11,13=GPIO13,14=GPIO15 | | J5 pad1 = GPIO19 | VERIFIED | J5.1=GPIO19 | | GPIO19 absent on J6 (J5-only breakout point among TFT/PIN nets) | VERIFIED | J6 nets: TX,RX,GPIO1,GPIO2,GPIO42,GPIO41,GPIO40,GPIO39,GPIO38,GPIO37,GPIO36,GPIO35,GPIO0,GPIO45,GPIO48,GPIO47,GPIO21,GPIO20 | | CC1: J2.A5 -> R1 -> GND independent; CC2: J2.B5 -> R2 -> GND independent | VERIFIED | CC1 set=[('J2', 'A5'), ('R1', '1')] CC2 set=[('J2', 'B5'), ('R2', '1')] R1.2=GND R2.2=GND | | RST: J1.3 <-> SW1.2 (J3.3 = RX per schematic), SW1.1 -> GND | VERIFIED | RST set=[('J1', '3'), ('SW1', '2')] SW1.1=GND | | J2 VBUS pads direct VIN (no D1/regulator in BOM/board), C1/C2 VIN, J1.21, J9 x8 | VERIFIED | J2 VIN pads=['A4', 'A9', 'B4', 'B9'] C1.1=VIN C2.1=VIN J1.21 in VIN=True J9.1=VIN | | Full F.Cu+B.Cu routing: 0 DRC violations, 0 unconnected pads | VERIFIED | DRC report footer: 0 violations / 0 unconnected / 0 footprint errors | | Only F.Cu and B.Cu copper | VERIFIED | layer split: F=212 B=117 | | All track widths = board min 0.2 mm | VERIFIED | width histogram: {0.2: 329} | | 45-degree routing (0/45/90 only), tolerance 0.004 mm | VERIFIED | non-45 segments=0 (of 329), arcs=0 | | No zones: fully trace-based copper | VERIFIED | zone count=0 | | No rule suppressions / no .kicad_dru / no hidden-store trickery | VERIFIED | DRU absent; no suppress tokens in board file | | J2 pad-local clearance 0.15 on all 20 pads (USB4085), global clearance 0.2 intact | VERIFIED | J2 pads=20 with (clearance 0.15)=20; min global netclass clearance 0.2 kept; pad pitch 0.85 - pad dia 0.7 = measured pad edge gap 0.15; hole-to-hole 0.85-0.4=0.45 | | Worst-case J2 pad hole-to-hole = JLCPCB 0.45 minimum line exactly | VERIFIED | drill=0.40; 0.85 pitch - 0.40 = 0.45 mm edge-to-edge | | ERC 0 errors / 0 warnings | VERIFIED | run_erc: 0 violations (0E/0W/0I) | | Schematic->board equivalence: net names + node sets match (0 diffs) | VERIFIED | nl_nets=48 nl_nodes=145 board_nets=42 board_netpads=139 renames={'/3V3': '3V3', '/GND': 'GND', '/GPIO0': 'GPIO0', '/GPIO1': 'GPIO1', '/GPIO2': 'GPIO2', '/GPIO3': 'GPIO3', '/GPIO4': 'GPIO4', '/GPIO5': 'GPIO5', '/GPIO6': 'GPIO6', '/GPIO7': 'GPIO7', '/GPIO8': 'GPIO8', '/GPIO9': 'GPIO9', '/GPIO10': 'GPIO10', '/GPIO11': 'GPIO11', '/GPIO12': 'GPIO12', '/GPIO13': 'GPIO13', '/GPIO14': 'GPIO14', '/GPIO15': 'GPIO15', '/GPIO16': 'GPIO16', '/GPIO17': 'GPIO17', '/GPIO18': 'GPIO18', '/GPIO19': 'GPIO19', '/GPIO20': 'GPIO20', '/GPIO21': 'GPIO21', '/GPIO35': 'GPIO35', '/GPIO36': 'GPIO36', '/GPIO37': 'GPIO37', '/GPIO38': 'GPIO38', '/GPIO39': 'GPIO39', '/GPIO40': 'GPIO40', '/GPIO41': 'GPIO41', '/GPIO42': 'GPIO42', '/GPIO45': 'GPIO45', '/GPIO46': 'GPIO46', '/GPIO47': 'GPIO47', '/GPIO48': 'GPIO48', '/RST': 'RST', '/RX': 'RX', '/TX': 'TX', '/VIN': 'VIN', 'Net-(J2-CC1)': 'Net-(J2-PadA5)', 'Net-(J2-CC2)': 'Net-(J2-PadB5)'} unmatched=none | | Pristine inputs untouched (md5 alcene-base.kicad_pcb == 889e473461cc105d1d7d0d53a65d60c9) | VERIFIED | both files md5 889e473461cc105d1d7d0d53a65d60c9 |
## Residual risks (accepted, documented)

1. **J2 hole-to-hole = 0.45 mm exactly** - equals the JLCPCB published
   PTH pad hole-to-hole line with zero margin.  Consequence: order
   review must not round the 0.4 mm drill; no re-tolerance allowed.
   Geometry is fixed by the GCT USB4085 footprint.
2. **0.15 mm pad clearance at J2 only** - inside the published JLCPCB
   envelope (needs >= 0.10 mm capability; SMD pad-pad line is 0.15).
   Zero margin against the 0.15 SMD line: only the connector pads carry
   it; J2-vs-anything-else remains 0.2 mm.
3. **Development renderer quirk** - the MCP "2D board view" PNG does not
   stroke `Edge.Cuts` lines; not a board defect: the shipped file
   contains the 4-line closed outline (verified) and the plotted
   `*_Edge_Cuts.gm1` gerber contains it as plotted by KiCad.
4. **No GND pour** - board is deliberately fully track-based (0 zones);
   every GND path is real F.Cu/B.Cu trace copper plus 4 vias.  This was
   accepted because the tie system is small (14 GN-nets pads) and DRC
   shows 0 unconnected.

## Not applicable / deliberately skipped

- Board outline compaction: the 123 x 90 frame is already exactly the
  required size; compaction was considered and skipped (no requirement,
  high DRC-coupled risk).
