int flame = 2;
int led = 11;
int state = 0;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(flame, INPUT);
  Serial.begin(9600);
}

void loop() {
  state = digitalRead(flame);

  digitalWrite(led, LOW);

  if (state == 0) {
    Serial.println("fire!!");
    digitalWrite(led, HIGH);
    delay(3000);
  }else{

    Serial.println("fire scanning....");
    digitalWrite(led, LOW);
  }
  delay(3000`12);
}
