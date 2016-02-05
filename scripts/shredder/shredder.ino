#define SWITCH_PIN 11
#define REWIND_SWITCH_PIN 12
#define LED_PIN 13
#define SERVO_PIN 9

#include <Servo.h>

enum ShredderDirection {
  FORWARD,
  BACKWARD,
  STOP
};

Servo servo;

void setup() {
  pinMode(SWITCH_PIN, INPUT_PULLUP);
  pinMode(REWIND_SWITCH_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {

  int switchVal = digitalRead(SWITCH_PIN);
  int reverseSwitchVal = digitalRead(REWIND_SWITCH_PIN);
  
  if (switchVal == HIGH && reverseSwitchVal == HIGH) {
    digitalWrite(LED_PIN, LOW);
    setShredderDirection(FORWARD);
  } else if ( reverseSwitchVal == LOW) {
    setShredderDirection(BACKWARD);
  } else {
    digitalWrite(LED_PIN, HIGH);
    setShredderDirection(STOP);
  }

  delay(15);
}

void setShredderDirection(ShredderDirection direction) {
  
  if (direction == FORWARD) { // forward servo
    if (!servo.attached())
      servo.attach(SERVO_PIN);
    servo.write(0);
  } else if ( direction == BACKWARD ) { // rewind servo
    if (!servo.attached())
      servo.attach(SERVO_PIN);
    servo.write(180);
  } else { // stop servo
    if (servo.attached()) {
      servo.write(90);
      servo.detach();
    }
  } 
}

