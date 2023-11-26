int tr = 4;
int echo = 5;
void setup() {
  pinMode(tr, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(tr,HIGH);
  delay(1000);
  digitalWrite(tr,LOW);

  int distance = pulseIn(echo, HIGH)*340/2/10000;

  Serial.print(distance);
  Serial.println("cm");
  delay(100);
}
