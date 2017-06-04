/*
  Two switches DigitalReadSerial
 Reads a digital input on pin 8 and 9 prints the result to the serial

 */

// digital pin 2 has a pushbutton attached to it. Give it a name:
int pushButton = 8;
int pushButton2 = 9;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
  pinMode(pushButton2, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int buttonState = digitalRead(pushButton);
  int buttonState2 = digitalRead(pushButton2);
  // print out the state of the button:
  Serial.print("A=");
  Serial.print(buttonState);
  Serial.print("B=");
  Serial.println(buttonState2);
  delay(1);        // delay in between reads for stability
}



