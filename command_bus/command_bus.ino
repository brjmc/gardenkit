#include <arduino.h>

// PINS
#define US_TRIGGER 2
#define US_ECHO 3

// COMMANDS
#define READ_TANK '1'

// VARIABLES
int command;
float duration;
float distance;

float readTankLevel() {
    digitalWrite(US_TRIGGER, LOW);
    delayMicroseconds(1);
    digitalWrite(US_TRIGGER, HIGH);
    delayMicroseconds(5);
    digitalWrite(US_TRIGGER, LOW);
    duration = pulseIn(US_ECHO, HIGH);
    distance= duration*0.034/2;
    return distance;
}

void setup() {
  pinMode(US_TRIGGER, OUTPUT);
  pinMode(US_ECHO, INPUT);
  Serial.begin(9600);
  delay(20);
}


void loop() {
  while(Serial.available()) {
    command = Serial.read();
    switch(command) {
      case READ_TANK:
        Serial.println(readTankLevel());
        break;
      default:
        Serial.println(-9999);
        break;
    }
  }
}