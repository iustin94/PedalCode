#include <Arduino.h>

const int SWITCH_A = 4;
const int SWITCH_B = 5;

void setup() {
  Serial.begin(9600);
  pinMode(SWITCH_A, INPUT_PULLUP);
  pinMode(SWITCH_B, INPUT_PULLUP);
}

void loop() {
  bool a = digitalRead(SWITCH_A) == LOW;
  bool b = digitalRead(SWITCH_B) == LOW;

  Serial.print(a);
  Serial.println(b);

  delay(10);
}
