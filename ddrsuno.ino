const int ledPin = 9;
const int motPin = 8;

void setup() {
  Serial.begin(9600);
  delay(2000);  // Allow Arduino to stabilize
  pinMode(ledPin, OUTPUT);
  pinMode(motPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    Serial.println(command);  // Debugging output

    if (command == '1') {  // Eyes closed
      digitalWrite(ledPin, HIGH);
      digitalWrite(motPin, HIGH);
    } else if (command == '0') {  // Eyes open
      digitalWrite(ledPin, LOW);
      digitalWrite(motPin, LOW);
    }
  }
}
