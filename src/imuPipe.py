#!/usr/bin/env python3
import rospy
import csv
import serial
from sensor_msgs.msg import Imu
try:
    print("Opening Serial Port")
    ser = serial.Serial('/dev/ttyACM1', 9600)
    print("Done with opening port:" + ser.name)
    sensor_buffer = []



    rospy.init_node('gps_reader')
    pub = rospy.Publisher('/dfimu/data', Imu, queue_size=10)
    while not rospy.is_shutdown():
        try:
            arduino_data = ser.read(100)
            #float(ser.readline().decode(‘ascii’).strip())
            print(arduino_data)
            #sensor_buffer.append(arduino_data)
        except ValueError:
            print("Received invalid sensor data")
            continue
except KeyboardInterrupt:
    pass
finally:
    if ser:
        ser.close()
    rospy.signal_shutdown("Program stopped by user")