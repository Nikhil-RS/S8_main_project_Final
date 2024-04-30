const int sensorPin = 2;  // Connect the sensor to digital pin 2
int vibrationState = 0;   // Variable to store the vibration state
#include <SoftwareSerial.h>

SoftwareSerial gpsSerial(0, 1); // RX, TX

void setup() {
  Serial.begin(9600);
  gpsSerial.begin(9600);   
    // Initialize serial communication at 9600 bits per second
  pinMode(sensorPin, INPUT); // Set the sensor pin as input
}

void loop() {
  // Read the state of the vibration sensor
  vibrationState = digitalRead(sensorPin);

  // Check if vibration is detected
  if (vibrationState == HIGH) {
    Serial.println("Accident");
    
    if (gpsSerial.available() > 0) {
    if (gpsSerial.find("$GPRMC")) {
      String data = gpsSerial.readStringUntil('\n');
      Serial.println(data);
    }
  }

    // Add your code here to perform actions when vibration is detected
  }
  else{
    Serial.println("nil");
  }
  

  delay(100);  // Delay for stability
}
