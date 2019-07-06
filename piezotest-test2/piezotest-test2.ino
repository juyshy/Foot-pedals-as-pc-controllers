// debugging threshold levels
const int sensorPin = 0;
const int sensorPin2= 1;
const int sensorPin3= 2;
const int sensorPin4= 3;
const int sensorPin5= 4;
const int threshold = 120;
void setup()
{ 
  Serial.begin(9600);      // sets the serial port to 9600
  pinMode( 0, INPUT);
  pinMode( 1, INPUT);
  //pinMode(ledPin, OUTPUT);
}
void loop()
{
  int val = analogRead(sensorPin);
  int val2 = analogRead(sensorPin2);
  int val3 = analogRead(sensorPin3);
  int val4 = analogRead(sensorPin4);
  int val5 = analogRead(sensorPin5); 
  //Serial.println(val, DEC);
  if (val >= threshold)
  {
    Serial.println(1, DEC);
    Serial.println(val, DEC);
    delay(300);
  }
    if (val2 >= 350)
  {
    Serial.println(2, DEC);
    Serial.println(val2, DEC);
    delay(300);
  }
    if (val3 >= threshold)
  {
    Serial.println(3, DEC);
    Serial.println(val3, DEC);
    delay(300);
  }
    if (val4 >= threshold)
  {
    Serial.println(4, DEC);
    Serial.println(val4, DEC);
    delay(300);
  }
    if (val5 >= threshold)
  {
    Serial.println(5, DEC);
    Serial.println(val5, DEC);
    delay(300);
  }
}
