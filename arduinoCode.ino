/**************************************************
Arduino code. Requires a arduino board with at minimum two digital pins (light and switch button on pressable joystick) and two analog pwm pins for the joystick

Led could be removed, or use board supplied led if available.
 ********************************************************/

const int xPin = A0;  //the VRX attach to
const int yPin = A1;  //the VRY attach to
const int swPin = 8;  //the SW attach to
const int ledPin = 9; // why not have a green led light glow when you move one direction.

void setup()
{
  pinMode(swPin, INPUT);  //set the SW pin to INPUT
  digitalWrite(swPin, HIGH);   //And initial value is HIGH
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop()
{
  Serial.print("X: "); 
  Serial.print(analogRead(xPin));  // print the value of VRX in DEC
  Serial.print("|Y: ");
  Serial.print(analogRead(yPin));  // print the value of VRX in DEC
  Serial.print("|Z: ");
  Serial.println(digitalRead(swPin));   // print the value of SW
  delay(500);
  if (analogRead(xPin) < 400){
    digitalWrite(ledPin,HIGH);
  }
  if (analogRead(xPin) > 800){
    digitalWrite(ledPin,LOW);
  }


  
}
