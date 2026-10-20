# alcene-board-v1 Power-Path Analysis

## 1. Intended versus actual power path

Intended path from design statement:
`J2 VBUS -> D1 (onsemi SS14) -> /VIN`

Actual path in current schematic:
`J2 VBUS -> /VIN` directly

D1 is absent from the current schematic. This is a concrete implementation defect relative to the documented design.

## 2. D1 identity and polarity evidence

Evidence from project backup schematic `kicad-backup-20261020-171051/kicad/alcene-board-v1.kicad_sch`:
- Symbol: `Device:D_Schottky`
- Value: `SS14 (onsemi, 40V 1A Schottky)`
- Manufacturer: onsemi
- MPN: SS14
- Package: SMA (DO-214AC)
- Footprint: `Diode_SMD:D_SMA`
- VRRM: 40 V
- Average forward current: 1 A
- VF max: 0.5 V at 1 A
- Pin 1 = cathode (K)
- Pin 2 = anode (A)

Datasheet verification:
- onsemi SS12-SS100 family datasheet lists SS14 as 40 V VRRM, 1.0 A average forward current.
- VF maximum is 500 mV at IF = 1.0 A, TA = 25 C.
- Reverse current maximum is 0.2 mA at rated VR, TA = 25 C.
- Package is DO-214AC (SMA), cathode denoted by color band.

Polarity in the backup schematic:
- D1 rotated 180 degrees at (88.9, 144.78).
- Pin 2 (anode) connects to J2 VBUS side.
- Pin 1 (cathode) connects to VIN side.
- Therefore the intended orientation is correct: anode toward USB VBUS, cathode toward VIN.

If D1 is reinstated, the same orientation must be preserved.

## 3. Forward voltage drop and downstream voltage

Assumptions:
- USB VBUS nominal: 5.00 V.
- USB VBUS allowed range: 4.75 V to 5.25 V.
- Cable and connector loss estimate: 0.1 V to 0.3 V.
- SS14 VF at light load (about 0.1 A): approximately 0.2 V to 0.3 V typical.
- SS14 VF at typical load (about 0.3 A to 0.5 A): approximately 0.35 V to 0.45 V typical.
- SS14 VF worst case at 1 A: 0.5 V maximum.

Estimated VIN if D1 is reinstated:
- Light load: 5.00 - 0.2 - 0.15 = 4.65 V
- Typical load: 5.00 - 0.4 - 0.2 = 4.40 V
- Heavy load near 1 A: 5.00 - 0.5 - 0.3 = 4.20 V
- Worst-case source: 4.75 - 0.5 - 0.3 = 3.95 V

The DevKit uses an AMS1117-3.3 class LDO with dropout in the range of approximately 1.0 V to 1.3 V. Stable 3.3 V regulation therefore requires VIN at or above approximately 4.3 V to 4.6 V. The intended diode path has limited margin, especially at high current or low source voltage.

Current schematic has no diode, so VIN is approximately USB VBUS minus cable loss. That gives more voltage margin but removes reverse-current protection.

## 4. Current budget

Estimated loads:
- ESP32-S3 module active with Wi-Fi TX: approximately 240 mA to 310 mA peak.
- DevKit USB-UART and regulator quiescent: approximately 5 mA to 10 mA.
- TFT logic and touch controller: approximately 20 mA to 50 mA.
- TFT backlight: current unknown. Many small ILI9341 modules draw roughly 20 mA to 80 mA, but this is not verified for the actual module.
- Breakout header loads: unknown and user-dependent.

Planning estimate:
- Typical active load: 300 mA to 400 mA.
- Peak load with Wi-Fi TX and backlight: 400 mA to 600 mA.
- Design limit should not exceed 500 mA unless USB source-current detection and a compatible source are implemented.

USB-C sink configuration:
- Two 5.1 kohm CC pull-down resistors identify a basic USB Type-C sink (UFP).
- This identifies default USB power capability only.
- It does not by itself detect or negotiate 1.5 A or 3 A source capability.
- Therefore the design should be treated as a 500 mA default-USB-power design unless source-current detection is added and verified.

## 5. Power-source combination matrix

| Source A | Source B | Shared rail | Potential path | Risk | Status |
|---|---|---|---|---|---|
| J2 USB-C | J9 external supply | VIN | If D1 absent, J9 can feed USB VBUS and DevKit. If D1 present, D1 blocks J9 to USB but J9 still feeds DevKit VIN. | Backfeeding USB port without D1; contention without load sharing. | FAIL without D1; CONDITIONAL with D1 and documented policy |
| J2 USB-C | DevKit 3V3 pins | 3V3 | 3V3 pin can drive DevKit rail while USB regulator is active. | Regulator/source contention, possible damage. | Prohibited |
| J9 external supply | DevKit 3V3 pins | VIN and 3V3 | Both can energize rails simultaneously. | Uncontrolled source contention. | Prohibited |
| J2 USB-C | DevKit USB port | 5V/VIN | Both USB inputs can power same VIN rail. | Dual USB source contention. | Prohibited unless only one is connected |
| External 3V3 on J8 | DevKit USB | 3V3 | External 3V3 can backpower DevKit and its regulator. | Regulator backpowering. | Prohibited |
| J2 USB-C only | None | VIN/3V3 | Normal intended path. | None if within current and voltage limits. | Allowed |

D1 does not make every simultaneous-source combination safe. It only blocks reverse current from VIN to USB VBUS if it is present and correctly oriented.

## 6. C1 and C2 audit

- C1: 10 uF, 0805, connected from VIN/USB_VBUS to GND.
- C2: 100 nF, 0805, connected from VIN/USB_VBUS to GND.
- Both are on the USB VBUS side in the current schematic, upstream of the intended diode position.
- Voltage rating is not recorded. For a 5 V USB environment, a minimum rating of 10 V is required; 16 V or 25 V is preferred.
- Dielectric and tolerance are not recorded.
- No downstream capacitance is provided after the intended diode. This is an engineering consideration, not an automatic schematic change.

## 7. DevKit power-input compatibility

- J1 pin 21 is the DevKit 5V input. Schematic connects VIN to this pin.
- J1 pins 1 and 2 are 3V3 outputs. Schematic connects them to /3V3.
- J1 pin 22 is GND.
- The DevKit's 5V-to-3.3V regulator is an AMS1117-3.3 class device with dropout around 1.0 V to 1.3 V.
- Therefore the intended diode path must maintain VIN above approximately 4.3 V to 4.6 V for stable 3.3 V output.

## 8. Items requiring post-assembly measurement

- Actual SS14 forward drop at the real load current and temperature.
- Actual USB source voltage at the board under load.
- DevKit 3.3 V rail stability during Wi-Fi TX peaks.
- TFT backlight current.
- Thermal behavior of D1 at maximum current.
- Whether the selected C1/C2 parts meet their intended voltage rating.