
/*!
   @file getLightIntensity.ino
   @Set the frequency of data output by the sensor, read the acceleration, angular velocity, and angle of X, Y, and Z axes.
   @n Experimental phenomenon: when the sensor starts, it outputs data at the set frequency and the data will be displayed on serial monitor
   @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
   @licence     The MIT License (MIT)
   @author [huyujie](yujie.hu@dfrobot.com)
   @version  V1.0
   @date  2020-12-03
   @https://github.com/DFRobot
*/
#include <DFRobot_WT61PC.h>
#include <SoftwareSerial.h>

//Use software serial port RX：10，TX：11
SoftwareSerial mySerial(10, 11);

DFRobot_WT61PC sensor(&mySerial);

void setup()
{
  //Use Serial as debugging serial port 
  Serial.begin(115200);
  //Use software serial port mySerial as communication seiral port 
  mySerial.begin(9600);
  //Revise the data output data frequncy of sensor FREQUENCY_0_1HZ for 0.1Hz, FREQUENCY_0_5HZ for 0.5Hz, FREQUENCY_1HZ for 1Hz, FREQUENCY_2HZ for 2Hz, 
  //                        FREQUENCY_5HZ for 5Hz, FREQUENCY_10HZ for 10Hz, FREQUENCY_20HZ for 20Hz, FREQUENCY_50HZ for 50Hz, 
  //                        FREQUENCY_100HZ for 100Hz, FREQUENCY_125HZ for 125Hz, FREQUENCY_200HZ for 200Hz.
  sensor.modifyFrequency(FREQUENCY_10HZ);
}


void loop()
{
  if (sensor.available()) {
    Serial.print("Acc\t"); Serial.print(sensor.Acc.X); Serial.print("\t"); Serial.print(sensor.Acc.Y); Serial.print("\t"); Serial.println(sensor.Acc.Z); //acceleration information of X,Y,Z
    Serial.print("Gyro\t"); Serial.print(sensor.Gyro.X); Serial.print("\t"); Serial.print(sensor.Gyro.Y); Serial.print("\t"); Serial.println(sensor.Gyro.Z); //angular velocity information of X,Y,Z
    Serial.print("Angle\t"); Serial.print(sensor.Angle.X); Serial.print("\t"); Serial.print(sensor.Angle.Y); Serial.print("\t"); Serial.println(sensor.Angle.Z); //angle information of X, Y, Z 
    Serial.println(" ");
  }
}


