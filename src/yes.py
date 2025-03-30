#!/usr/bin/env python
import rospy


rospy.init_node("hello_node")

while not rospy.is_shutdown():
    rospy.loginfo("Team-Ros is here")


