#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
    move = Twist()
    angles = msg.ranges
    right_idx = int(( -math.pi/2 - msg.angle_min ) / msg.angle_increment)
    front_idx = int(( 0 - msg.angle_min ) / msg.angle_increment)
    left_idx = int(( math.pi/2 - msg.angle_min ) / msg.angle_increment)
    right = angles[right_idx]
    front = angles[front_idx]
    left = angles[left_idx]
    if right < 1:
        move.angular.z = 0.5
        print("Turning left")
    elif left < 1:
        move.angular.z = -0.5
        print("Turning right")
    elif front < 1:
        move.angular.z = 0.5
        print("Turning left")
    else:
        move.linear.x = 0.5
        print("Moving forward")
    pub.publish(move)

rospy.init_node("angles_node", anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
