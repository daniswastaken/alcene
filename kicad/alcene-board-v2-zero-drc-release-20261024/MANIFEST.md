# MANIFEST - alcene-board-v2 zero-DRC release (2026-10-24)

Release dir: `X:\alcene\kicad\alcene-board-v2-zero-drc-release-20261024\`

## Shipped board (in kicad dir, referenced by this release)

`alcene-board-v2-rebased-zero-drc.kicad_pcb` - 240632 bytes, sha256 `e37d07e445ab54b6ecb122d758fe6ff959218ac0c149eb0c26fb81fc70bfceb5`

This exact file passed the final on-disk DRC:
0 errors / 0 warnings / 0 unconnected (`alcene-board-v2-final-drc-report.txt`).

## Pristine inputs (unmodified, md5-verified)

| File | md5 |
|---|---|
| `alcene-base.kicad_pcb` | `889e473461cc105d1d7d0d53a65d60c9` |
| `alcene-base-source-backup-20261024.kicad_pcb` | `889e473461cc105d1d7d0d53a65d60c9` |

## Fabrication package

- Gerbers: 9 layers (F/B Cu, F/B Mask, F/B Silk, F Paste, User.Drawings, Edge.Cuts) + `job.gbrjob`
- Drill: `alcene-board-v2-rebased-zero-drc.drl` (merged Excellon incl. vias) + `-drl_map.pdf`
- Fab-relevant gerber files: `*_F_Cu.gtl, *_B_Cu.gbl, *_F_Mask.gts, *_B_Mask.gbs,
  *_F_Silkscreen.gto, *_B_Silkscreen.gbo, *_Edge_Cuts.gm1`

## Reports

DRC/ERC/QC/equivalence/clearance/connectivity/pinout/BOM in this directory (below).

## File list (sha256)

| File | Bytes | sha256 |
|---|---|---|
| `alcene-board-v2-bom.csv` | 1069 | `aa2c361006590a0718359603581f0e577212813f594d0921830dabd5e1fbf2ef` |
| `alcene-board-v2-clearance-disposition.md` | 3226 | `91bda2c117247889cc90064b38d2ee09ff26cde606908a7c30468b242bf3768e` |
| `alcene-board-v2-final-drc-report.txt` | 533 | `ba3494e01f585b60489ee3506ca29ff809a00b9cbbdddc825da57190a5ebd3c5` |
| `alcene-board-v2-final-erc-report.txt` | 896 | `36d445cea6033544202eeef7017bc532cd345f701f987dc3198916c8210956d5` |
| `alcene-board-v2-j4-pinout.md` | 919 | `8a7074431b01b50ba36de4ca4de8e3341b0a0b5819d982fe07010c1b7d548ef2` |
| `alcene-board-v2-netlist.net` | 43751 | `c07518079d18f301098da5adf4a3d20506afc114d6be7472113d3bc31664fcfb` |
| `alcene-board-v2-production-qc-report.md` | 6260 | `2b3aea60393c4344b8a76f85d9835b4bb085f5efd0853bce31f28b7516d55c7a` |
| `alcene-board-v2-real-copper-connectivity.md` | 4376 | `19379327a65627bef6d3101f5dd6ed4bc9f649de54af1da1a4406592657efa6d` |
| `alcene-board-v2-rebased-zero-drc-B_Cu.gbl` | 14807 | `faf8f4c706d24760cb0e95e3653b34d886cd412867b9d5b017624553a6ea1c27` |
| `alcene-board-v2-rebased-zero-drc-B_Mask.gbs` | 4635 | `8fb3afc1ee626c2a4c493ee3afb69b0ab02b88168de3ef76f9e4f31d67355582` |
| `alcene-board-v2-rebased-zero-drc-B_Silkscreen.gbo` | 58682 | `7da514b4c0e0525bae44313f6a7ceff922bfcddde1368c2a7275d22d26b1bfb1` |
| `alcene-board-v2-rebased-zero-drc-Edge_Cuts.gm1` | 733 | `59b0ef10091bdab1cf40fa12865b497c26214a4a3aa1dbc5309a771d8efe617d` |
| `alcene-board-v2-rebased-zero-drc-F_Cu.gtl` | 21768 | `75478b8a439c28153b0bce4b208958eb75dc4df446daff4d455ccb56a39fae0c` |
| `alcene-board-v2-rebased-zero-drc-F_Mask.gts` | 5904 | `cb34ad037203ed327c468f79e5400706cdb6c54858670782bae7a54dcc57883b` |
| `alcene-board-v2-rebased-zero-drc-F_Paste.gtp` | 1761 | `98ed334f96df93c264b049eff8b2bb1fec2169d42710288d36de5be245ee5c9f` |
| `alcene-board-v2-rebased-zero-drc-F_Silkscreen.gto` | 160507 | `8cdcee8ff15fd0e81f930e3a9b7aa0f766a13814a69cadce54c2cb063bce6167` |
| `alcene-board-v2-rebased-zero-drc-User_Drawings.gbr` | 27305 | `edafd2c66dae35ad99b526e60f34c53c1ad0a077736df6d8ff6513eba7d1a3ea` |
| `alcene-board-v2-rebased-zero-drc-drl_map.pdf` | 19720 | `326b82fc9444fe68c46b424bbc9f0c4a758b8bc1f30d37da658bc69e7eef105e` |
| `alcene-board-v2-rebased-zero-drc-job.gbrjob` | 2998 | `1db0c1316104dfff3e925926f30c5c11099ecdfa2dd24dadd09c9ac9facbb4f0` |
| `alcene-board-v2-rebased-zero-drc.drl` | 2953 | `26e18db6e30f95629ac13c06c7e7773a13f11f9c876802d9351d775e04515f60` |
| `alcene-board-v2-schematic-pcb-equivalence.md` | 5245 | `2ae0b501cfc52cdfb8fa01b7c1e1b5a723030481cbc8ce132d7486ebf63c663d` |
## Tool chain

- KiCad 10.0 (kicad-cli 10.0), KiCad MCP (swig backend), freerouting v2.5.0 (jar autosource).
- Reports generated 2026-10-24 by `.opencode/gen_reports.py`; the board file was
  not modified during report generation (mtime invariant checked).
