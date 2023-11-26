#include <Servo.h>

Servo servoRight;
Servo servoLeft;

int flame = 2;
int led = 7;
int led2 = 11;
int buzzer = 8;
int state = 0;
int tr = 4;
int echo = 3;
int REC = 6;
int PLAYE = 5;
char input = 0;

void setup() {
  servoLeft.attach(13);
  servoRight.attach(12);
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(flame, INPUT);
  pinMode(tr, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(REC,OUTPUT);
  pinMode(PLAYE,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()) {

    input = Serial.read();
    switch(input) {
      case 'R':
        digitalWrite(REC,HIGH);
        break;
      case 'S':
        digitalWrite(REC,LOW);
        break;
    }
  }
  state = digitalRead(flame);

  digitalWrite(led, LOW);
  noTone(buzzer);
  maneuver(200, 200, 0);

  if (state == 0) {
    digitalWrite(led, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(PLAYE,HIGH);
    delay(10);
    digitalWrite(PLAYE,LOW);
    tone(buzzer, 5000, 4000);
    maneuver(0, 0, 0);;
    maneuver(-200, -200, 500); 
    maneuver(-200, 200, 1900);
    maneuver(200, 200, 3000);
    maneuver(-200, 200, 1000);
    maneuver(200, 200, 4000);
    maneuver(-200, 200, 1000);
    maneuver(200, 200, 6000);
    maneuver(-200, 200, 1000);
    maneuver(200, 200, 100);
  }else{
    digitalWrite(led, LOW);
    digitalWrite(led2, LOW);
    noTone(buzzer);
  }
  delay(100);
  
  digitalWrite(tr,HIGH);
  delay(1000);
  digitalWrite(tr,LOW);

  int distance = pulseIn(echo, HIGH)*340/2/10000;

  Serial.print(distance);
  Serial.println("cm");
  delay(100);
  
  if (distance <= 20) {
     maneuver(200, -200, 1000);
  }
}
void maneuver(int speedLeft, int speedRight, int msTime)
    {
servoLeft.writeMicroseconds(1500+speedLeft); // Set Left servo speed
servoRight.writeMicroseconds(1500-speedRight);//Set right servo speed
if(msTime==-1) // if msTime = -1
{ 
servoLeft.detach(); // Stop servo signals
servoRight.detach(); 
}
delay(msTime); // Delay for msTime
}