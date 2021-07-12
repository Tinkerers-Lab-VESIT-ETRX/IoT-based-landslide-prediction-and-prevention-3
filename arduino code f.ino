#include<DHT.h>

int SensorPin=A0;
#define dht_1 A1
#define DHTTYPE DHT11
DHT dht(dht_1,DHTTYPE);


// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second: 
  Serial.begin(9600);
  dht.begin();
}

// the loop routine runs over and over again forever:
void loop() {

{
  int SensorValue = analogRead(SensorPin);   
  float SensorVolts = analogRead(SensorPin)*0.0048828125;
  float temp =dht.readTemperature();
  float Humid = dht.readHumidity();
  Serial.print("Moisture = ");Serial.print((int)SensorVolts);Serial.print("v,");
  Serial.print("Temp = ");Serial.print((int)temp);Serial.print("v,");
  Serial.print("Humid = ");Serial.print((int)Humid);
   // Serial.print("    |    ");
  // Serial.print("moisture = "); // Displaying moisture // Serial.print(SensorValue);// Serial.print("v");
  Serial.println();
  delay(1000);
}
}


  
