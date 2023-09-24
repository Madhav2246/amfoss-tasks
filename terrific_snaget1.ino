#include <Servo.h>
#include <LiquidCrystal.h>

Servo servoMotor;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int ldrPin = A0;     
int threshold = 500; 
int servoAngle = 90;
void setup() {
  servoMotor.attach(9);
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Radiant Plant: OFF");
}

void loop() {
  int lightLevel = analogRead(ldrPin);

  if (lightLevel > threshold) {
    
    if (servoAngle < 90) {
      servoAngle++; 
      servoMotor.write(servoAngle);
    }
    lcd.setCursor(0, 0);
    lcd.print("Radiant Plant: ON ");
    lcd.setCursor(0, 1);
    lcd.print("Light Level: ");
    lcd.print(lightLevel);
  } else {
    
    if (servoAngle > 0) {
      servoAngle--; 
      servoMotor.write(servoAngle);
    }
    lcd.setCursor(0, 0);
    lcd.print("Radiant Plant: OFF");
    lcd.setCursor(0, 1);
    lcd.print("Light Level: ");
    lcd.print(lightLevel);
  }

  delay(100); 
}
