# alcene-board-v1 Power-Path Analysis — Final Revision

- Schematic: `X:\alcene\kicad\alcene-board-v1.kicad_sch`
- KiCad version: 10.0.7
- Date: 2026-10-20

## 1. Final power architecture

`J2 USB-C VBUS -> VIN -> J1 pin 21 and J9 pins 1-8`

- D1 is intentionally omitted.
- No series Schottky diode is present.
- No reverse-current blocking is provided between J2 VBUS and VIN.
- C1 and C2 are connected between VIN and GND.
- J8 and J9 are distribution outputs only.

## 2. Source voltage range

- USB VBUS nominal: 5.00 V.
- USB VBUS allowed range: 4.75 V to 5.25 V.
- Cable and connector loss estimate: 0.1 V to 0.3 V.
- Direct path VIN estimate: 4.7 V to 5.0 V under typical conditions.
- The direct path improves regulator input-voltage margin relative to the previously considered SS14 path, which had a 0.5 V maximum forward drop.

## 3. Current budget

Estimated loads:
- ESP32-S3 module active with Wi-Fi TX: approximately 240 mA to 310 mA peak.
- DevKit USB-UART and regulator quiescent: approximately 5 mA to 10 mA.
- TFT logic and touch controller: approximately 20 mA to 50 mA.
- TFT backlight: owner-confirmed direct 3V3 connection; exact current not independently verified. Typical small ILI9341 backlight loads are often 20 mA to 80 mA.
- External header loads: user-dependent and not fixed by the schematic.

Planning estimate:
- Typical active load: approximately 300 mA to 400 mA.
- Peak load with Wi-Fi TX and backlight: approximately 400 mA to 600 mA.

USB-C sink:
- Two 5.1 kohm CC pull-down resistors implement a basic USB Type-C sink.
- This does not independently detect or negotiate 1.5 A or 3 A source capability.
- The design must not be described as supporting arbitrary USB-C high-current operation.

## 4. Power-source policy

- J2 is the external power input.
- J8 3V3 and J9 VIN are distribution outputs only.
- Do not inject external power through J8 or J9.
- Do not connect J2 USB power and DevKit native USB power simultaneously.
- DevKit power inputs are mutually exclusive.

J8/J9 output-only operation does not make simultaneous arbitrary source combinations safe.

## 5. Capacitors

- C1: Murata `GRM21BZ71E106KE15L`, 10 uF, 25 V, X7R, +/-10%, 0805.
- C2: Murata `GRM21BR71H104KA01L`, 100 nF, 50 V, X7R, +/-10%, 0805.
- C1 DC-bias derating must be checked in the Murata datasheet or SimSurfing; effective capacitance at 5 V may be below nominal.
- C2 is suitable for high-frequency decoupling on the 5 V rail.

## 6. DevKit compatibility

- J1 pin 21 receives VIN.
- J1 pins 1-2 provide 3V3.
- The DevKit uses an AMS1117-3.3 class regulator with dropout around 1.0 V to 1.3 V.
- Direct VBUS provides better regulator margin than the previously considered SS14 path.

## 7. Items requiring post-assembly verification

- Actual VIN under load.
- DevKit 3.3 V stability during Wi-Fi TX peaks.
- TFT backlight current.
- C1 effective capacitance under DC bias.
- Thermal behavior of connectors and traces at maximum current.