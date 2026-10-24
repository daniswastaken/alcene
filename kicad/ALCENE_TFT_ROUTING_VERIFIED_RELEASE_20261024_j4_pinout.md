# J4 Pinout Verification - ALCENE_TFT_ROUTING_VERIFIED_RELEASE_20261024

J4 is a 14-pin connector at (95.4257,113.25), rotation 90 degrees. Physical pads are ordered left-to-right as pad 1 through pad 14.

| Pad | Position (mm) | Net | Function |
|---|---|---|---|
| 1 | (95.4257,113.25) | 3V3 | VCC |
| 2 | (97.9657,113.25) | GND | Ground |
| 3 | (100.5057,113.25) | GPIO10 | LCD_CS |
| 4 | (103.0457,113.25) | GPIO8 | LCD_RST |
| 5 | (105.5857,113.25) | GPIO9 | LCD_DC |
| 6 | (108.1257,113.25) | GPIO11 | LCD_MOSI |
| 7 | (110.6657,113.25) | GPIO12 | LCD_CLK |
| 8 | (113.2057,113.25) | 3V3 | LCD_BL |
| 9 | (115.7457,113.25) | GPIO13 | LCD_MISO |
| 10 | (118.2857,113.25) | GPIO12 | TOUCH_CLK |
| 11 | (120.8257,113.25) | GPIO14 | TOUCH_CS |
| 12 | (123.3657,113.25) | GPIO11 | TOUCH_DIN |
| 13 | (125.9057,113.25) | GPIO13 | TOUCH_DOUT |
| 14 | (128.4457,113.25) | GPIO15 | TOUCH_IRQ |

Verified against fresh schematic netlist. Shared nets preserved: GPIO11 pads 6/12, GPIO12 pads 7/10, GPIO13 pads 9/13.