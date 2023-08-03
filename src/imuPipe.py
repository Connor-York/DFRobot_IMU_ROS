#!/usr/bin/env python3
import rospy
import csv
import serial
import tf
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion

try:
    print("Opening Serial Port")
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print("Done with opening port: " + ser.name)

    rospy.init_node('imu_pipe')
    print("Initialised ros node")

    rate = rospy.Rate(10)

    pub = rospy.Publisher('/dfimu/data', Imu, queue_size=10)

    print("Running ....")
    while not rospy.is_shutdown():
        try:
            arduino_data = ser.readline().decode('ascii').strip().split(",") # reads data and splits it by ","
            arduino_data = [float(value) for value in arduino_data] # converts the array of str to array of floats
            #print(arduino_data)
            #print(arduino_data[0])

            imu_msg = Imu()

            imu_msg.header.stamp = rospy.Time.now()
            imu_msg.header.frame_id = "imu2_frame"

            imu_msg.linear_acceleration.x = arduino_data[0]
            imu_msg.linear_acceleration.y = arduino_data[1]
            imu_msg.linear_acceleration.z = arduino_data[2]

            imu_msg.angular_velocity.x = arduino_data[3]
            imu_msg.angular_velocity.x = arduino_data[4]
            imu_msg.angular_velocity.x = arduino_data[5]

            quat = tf.transformations.quaternion_from_euler(arduino_data[6],arduino_data[7],arduino_data[8])
            Quat = Quaternion(*quat)

            imu_msg.orientation = Quat

            pub.publish(imu_msg)
            #print("publishing message")

            rate.sleep()

        except ValueError:
            print("Received invalid sensor data")
            continue

except KeyboardInterrupt:
    pass
finally:
    if ser:
        ser.close()
        print("Closing Serial Port")
    rospy.signal_shutdown("Program stopped by user")