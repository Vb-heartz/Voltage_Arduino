const int numchannels = 4;
const int sensorPin[] = {A0, A1, A2, A3};  // Define the analog pin to which the voltage source is connected
float voltage = 0.0;       // Variable to store the voltage value

void setup() {
  Serial.begin(9600);      // Initialize serial communication at 9600 baud }

void loop() {
 for ( int i=0; i<numchannels; i++){
 int sensorValue = analogRead(sensorPin[i]);  
 float voltage = sensorValue * (5.0 / 1023.0);   

  Serial.print(voltage);
  if(i<numchannels-1){
    Serial.print("\t");
  }
  }
  Serial.println();
  delay(1000);  // Wait for 1 second before taking another reading
}
