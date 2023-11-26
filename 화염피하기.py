#include <Servo.h>

Servo servoRight;
Servo servoLeft;

int flame = 2;
int led = 11;
int buzzer = 3;
int state = 0;

void setup() {
  servoLeft.attach(13);
  servoRight.attach(12);
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(flame, INPUT);

}

void loop() {
  
  state = digitalRead(flame);

  digitalWrite(led, LOW);
  noTone(buzzer);
  maneuver(200, 200, 0);

  if (state == 0) {
    digitalWrite(led, HIGH);
    tone(buzzer, 5000, 4000);
    maneuver(0, 0, 100);;
    maneuver(-200, -200, 1000); 
    maneuver(-200, 200, 2000);
  }else{
    digitalWrite(led, LOW);
    noTone(buzzer);
  }
  delay(100);
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