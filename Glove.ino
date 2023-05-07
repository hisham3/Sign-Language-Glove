/*
    MPU6050 Triple Axis Gyroscope & Accelerometer. Simple Gyroscope Example.
    Read more: http://www.jarzebski.pl/arduino/czujniki-i-sensory/3-osiowy-zyroskop-i-akcelerometr-mpu6050.html
    GIT: https://github.com/jarzebski/Arduino-MPU6050
    Web: http://www.jarzebski.pl
    (c) 2014 by Korneliusz Jarzebski
*/

#include <Wire.h>
#include <MPU6050.h>
#include <SoftwareSerial.h>

#define flex_1 A7
#define flex_2 A6
#define flex_3 A2
#define flex_4 A1
#define flex_5 A0

MPU6050 mpu;
SoftwareSerial BTSerial (1,0);

void setup() 
{
  BTSerial.begin(9600);

  // Initialize MPU6050
  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    delay(500);
  }
  
  // If you want, you can set gyroscope offsets
  // mpu.setGyroOffsetX(155);
  // mpu.setGyroOffsetY(15);
  // mpu.setGyroOffsetZ(15);
  
  // Calibrate gyroscope. The calibration must be at rest.
  // If you don't want calibrate, comment this line.
  mpu.calibrateGyro();

  // Set threshold sensivty. Default 3.
  // If you don't want use threshold, comment this line or set 0.
//  mpu.setThreshold(3);
}


void loop()
{
   Vector normGyro = mpu.readNormalizeGyro();
   Vector normAccel = mpu.readNormalizeAccel();
      
  int origin_flex1 = analogRead(flex_1);
  int origin_flex2 = analogRead(flex_2);
  int origin_flex3 = analogRead(flex_3);
  int origin_flex4 = analogRead(flex_4);
  int origin_flex5 = analogRead(flex_5);

//   map flex from 700,900 to 0,255
  int edited_flex1 = origin_flex1;
  int edited_flex2 = origin_flex2; //map(origin_flex2, 700, 900, 0, 255)
  int edited_flex3 = origin_flex3;
  int edited_flex4 = origin_flex4;
  int edited_flex5 = origin_flex5;
  
  if(BTSerial.available()> 0){
    char dataGet = BTSerial.read();
    if(dataGet == 'g'){
      BTSerial.print(edited_flex1);
      BTSerial.print(',');
      BTSerial.print(edited_flex2);
      BTSerial.print(',');
      BTSerial.print(edited_flex3);
      BTSerial.print(',');
      BTSerial.print(edited_flex4);
      BTSerial.print(',');
      BTSerial.print(edited_flex5);
      BTSerial.print(',');
      
      BTSerial.print(normGyro.XAxis);
      BTSerial.print(",");
      BTSerial.print(normGyro.YAxis);
      BTSerial.print(",");
      BTSerial.print(normGyro.ZAxis);
    
      BTSerial.print(",");
      BTSerial.print(normAccel.XAxis);
      BTSerial.print(",");
      BTSerial.print(normAccel.YAxis);
      BTSerial.print(",");
      BTSerial.println(normAccel.ZAxis);

    }
  }
delay(500);

}
