#include <Servo.h>

Servo servoDrill;

int led = 12;
int led2 = 13;
int tr = 9;
int echo = 10;
int buzzer = 4;
void setup() {
  pinMode(tr, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  Serial.begin(9600);
  servoDrill.attach(11);
}

void loop() {
  digitalWrite(tr,HIGH);
  delay(1000);
  digitalWrite(tr,LOW);
  digitalWrite(led,LOW);
  digitalWrite(led2,LOW);
  noTone(buzzer);

  int distance = pulseIn(echo, HIGH)*340/2/10000;

  Serial.print(distance);
  Serial.println("cm");
  delay(100);

  if (distance <= 15) {
    digitalWrite(led,HIGH);
    digitalWrite(led2,HIGH);
    delay(10);
    tone(buzzer, 5000, 4000);
    servoDrill.writeMicroseconds(1700);
  }else{
    digitalWrite(led,LOW);
    digitalWrite(led2,LOW);
    noTone(buzzer);
    servoDrill.writeMicroseconds(1500);
  }
}