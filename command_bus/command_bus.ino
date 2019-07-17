#include <arduino.h>

// PINS
#define US_TRIGGER 2
#define US_ECHO 3
#define VALVE_RELAY 3
#define MOISTURE_1 0
#define MOISTURE_2 1
#define MOISTURE_3 2
#define MOISTURE_4 3

// COMMAND CODES
#define READ_TANK '1'

#define READ_MOISTURE_1 '2'
#define READ_MOISTURE_2 '3'
#define READ_MOISTURE_3 '4'
#define READ_MOISTURE_4 '5'

#define OPEN_VALVE_30s '6'
#define OPEN_VALVE_5s '7'


// VARIABLES
int command;
float duration;
float distance;

float moisture;

bool openValve(int duration) {
  digitalWrite(VALVE_RELAY, HIGH);
  delay(duration);
  digitalWrite(VALVE_RELAY, LOW);
  return true;
}

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
  pinMode(MOISTURE_3, INPUT);
  pinMode(MOISTURE_4, INPUT);
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
      case READ_MOISTURE_3:
        Serial.println(readMoisture(MOISTURE_3));
        break;
      case READ_MOISTURE_4:
        Serial.println(readMoisture(MOISTURE_4));
        break;
      case OPEN_VALVE_30s:
        Serial.println(openValve(30000));
        break;
      case OPEN_VALVE_5s:
        Serial.println(openValve(5000));
        break;
      default:
        Serial.println(-9999);
        break;
    }
  }
}