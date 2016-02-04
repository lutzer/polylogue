#define SWITCH_PIN 12
#define LED_PIN 13
#define SERVO_PIN 9

#include <Servo.h>

Servo servo;

void setup() {
  pinMode(SWITCH_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);

  servo.attach(SERVO_PIN);

}

void loop() {

  int sensorVal = digitalRead(SWITCH_PIN);
  
  if (sensorVal == HIGH) {
    digitalWrite(LED_PIN, LOW);
    //servo.attach(SERVO_PIN);
    servo.write(180);
  } else {
    digitalWrite(LED_PIN, HIGH);
    servo.write(100);
  }

  delay(15);
}
