#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
   move = Twist()
   for r in msg.ranges:
       if r < 0.03:
         move.linear.x += 0.1
         rospy.loginfo(move.linear.x)
  #       move.angular.z = 0.1
   pub.publish(move)

rospy.init_node("odom_cmd", anonymous = True)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
sub = rospy.Subscriber("/scan", LaserScan, callback)
rate = rospy.Rate(1)
rate.sleep()
rospy.spin()
