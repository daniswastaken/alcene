//  alcene.ai -- ESP32-S3 boot splash
//
//  Brings up an I2C SSD1306 128x64 OLED and holds the alcene wordmark on it.
//  The panel keeps the last frame without refresh, so after setup() the splash
//  simply stays. Diagnostics go to Serial, never to the panel.
//
//  Wiring (see platformio.ini for the full pin map):
//      OLED SDA -> GPIO8      OLED SCL -> GPIO9
//
//  Everything on the S3 DevKitC-1 is 3.3 V only.

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_NeoPixel.h>
#include <Wire.h>

#include "alcene_wordmark.h"

namespace {

// The panel matches the wordmark framebuffer exactly; taking the dimensions
// from the generated header keeps a resolution change to a single source of
// truth. ALCENE_WORDMARK_W is 128, which is byte-aligned, so the generated
// bitmap needs no per-row padding.
constexpr int kWidth = ALCENE_WORDMARK_W;
constexpr int kHeight = ALCENE_WORDMARK_H;

// Stock S3 DevKitC-1 I2C pins. The 7-pin module also wants RES on GPIO10 and
// DC on GPIO11; the 4-pin module ties those and only needs SDA/SCL.
constexpr int kSdaPin = 8;
constexpr int kSclPin = 9;

constexpr uint8_t kOledAddress = 0x3C;
constexpr int kRgbPin = 48;
constexpr uint8_t kRgbCount = 1;

Adafruit_NeoPixel rgb(kRgbCount, kRgbPin, NEO_GRB + NEO_KHZ800);

// Reset pin is -1: the 4-pin module has no RES line, and the 7-pin one is
// clocked by the SSD1306's own charge-pump sequence well enough to come up.
Adafruit_SSD1306 display(kWidth, kHeight, &Wire, -1);

// The generated bitmap is already 128x64 with the wordmark centred inside it,
// so this is a straight full-panel blit. If the header ever carries art that is
// smaller than the panel, drawBitmap still anchors at the top-left, which is why
// centring is baked in at generation time rather than here.
void drawWordmark() {
  display.clearDisplay();
  display.drawBitmap(0, 0, ALCENE_WORDMARK, kWidth, kHeight, SSD1306_WHITE);
  display.display();
}

const char *revision() {
  switch (ESP.getChipRevision()) {
    case 0: return "0.0";
    case 1: return "0.1";
    case 2: return "0.2";
    default: return "?";
  }
}

void reportToSerial() {
  Serial.println();
  Serial.println(F("alcene.ai -- ESP32-S3"));
  Serial.print(F("  chip    : "));
  Serial.println(ESP.getChipModel());
  Serial.print(F("  rev     : "));
  Serial.println(revision());
  Serial.print(F("  cpu     : "));
  Serial.print(ESP.getCpuFreqMHz());
  Serial.println(F(" MHz"));
  Serial.print(F("  psram   : "));
  if (psramFound()) {
    Serial.print(ESP.getPsramSize() / (1024UL * 1024UL));
    Serial.println(F(" MB"));
  } else {
    Serial.println(F("not found -- check qio_opi in platformio.ini"));
  }
  Serial.print(F("  flash   : "));
  Serial.print(ESP.getFlashChipSize() / (1024UL * 1024UL));
  Serial.println(F(" MB"));
  Serial.print(F("  heap    : "));
  Serial.print(ESP.getFreeHeap() / 1024UL);
  Serial.println(F(" KB"));
  Serial.print(F("  oled    : "));
  Serial.println(display.width() * display.height() ? "ok" : "failed");
}

void halt(const __FlashStringHelper *why) {
  Serial.println(why);
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println(F("alcene.ai"));
  display.println();
  display.println(F("OLED not found"));
  display.println(F("check SDA=GPIO8"));
  display.println(F("SCL=GPIO9, addr 0x3C"));
  display.display();
  for (;;) {
    delay(1000);
  }
}

}  // namespace

void setup() {
  Serial.begin(115200);
  const uint32_t start = millis();
  while (!Serial && millis() - start < 2000) {
    delay(10);
  }

  rgb.begin();
  rgb.setBrightness(10);  // low, not blinding
  rgb.clear();
  rgb.show();

  Wire.begin(kSdaPin, kSclPin);
  Wire.setClock(400000);

  if (!display.begin(SSD1306_SWITCHCAPVCC, kOledAddress)) {
    halt(F("SSD1306 not responding at 0x3C."));
  }

  display.clearDisplay();
  display.display();
  delay(50);

  drawWordmark();
  reportToSerial();
}

void loop() {
  static int phase = 0;  // 0..599 full R→G→B→R
uint8_t r, g, b;
int p = phase % 600;
if (p < 200) {            // red → green
  r = 255 - p * 255 / 200;
  g = p * 255 / 200;
  b = 0;
} else if (p < 400) {     // green → blue
  p -= 200;
  r = 0;
  g = 255 - p * 255 / 200;
  b = p * 255 / 200;
} else {                  // blue → red
  p -= 400;
  r = p * 255 / 200;
  g = 0;
  b = 255 - p * 255 / 200;
}
rgb.setPixelColor(0, rgb.Color(r, g, b));
rgb.show();
phase += 6;             // 600/6 = 100 steps × 40ms = 4 s ring
if (phase >= 600) phase = 0;
delay(30);
}