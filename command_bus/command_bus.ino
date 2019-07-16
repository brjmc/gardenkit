#include <arduino.h>

// PINS
#define US_TRIGGER 2
#define US_ECHO 3
#define MOISTURE_1 0
#define MOISTURE_2 1

// COMMANDS
#define READ_TANK '1'
#define READ_MOISTURE_1 '2'
#define READ_MOISTURE_2 '3'

// VARIABLES
int command;
float duration;
float distance;

float moisture;

float readMoisture(int pin) {
 return analogRead(pin);
}

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
  pinMode(MOISTURE_1, INPUT);
  pinMode(MOISTURE_2, INPUT);
  pinMode(US_TRIGGER, OUTPUT);
  pinMode(US_ECHO, INPUT);
  Serial.begin(9600);
  delay(20);
}


void loop() {
  delay(1);
  while(Serial.available()) {
    command = Serial.read();
    switch(command) {
      case READ_TANK:
        Serial.println(readTankLevel());
        break;
      case READ_MOISTURE_1:
        Serial.println(readMoisture(MOISTURE_1));
        break;
      case READ_MOISTURE_2:
        Serial.println(readMoisture(MOISTURE_2));
        break;
      default:
        Serial.println(-9999);
        break;
    }
  }
}