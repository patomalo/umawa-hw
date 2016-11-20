byte number = 0;
const int ledPin = 13;
int ledState = LOW;
int a = 10;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

String concatVector(){
  return 
}
void loop(){
//if (Serial.available()) {
    Serial.print("value " + 112);
    if (ledState == LOW)
      ledState = HIGH;
    else
      ledState = LOW;
    // set the LED with the ledState of the variable:
    digitalWrite(ledPin, ledState);
    delay(5000);
 // }
}
