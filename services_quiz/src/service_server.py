#!/usr/bin/env python
import math
import rospy
from geometry_msgs.msg import Twist
from services_quiz.srv import RSquareServ, RSquareServResponse

pub = None

def move_square(side, reps):
    linear_speed = 0.2
    angular_speed = 0.5
    cmd = Twist()
    rate = rospy.Rate(10)
    for i in range(reps):
        for j in range(4):
            cmd.linear.x = linear_speed
            cmd.angular.z = 0.0
            t0 = rospy.Time.now().to_sec()
            while rospy.Time.now().to_sec() - t0 < side / linear_speed:
                pub.publish(cmd)
                rate.sleep()
            cmd.linear.x = 0.0
            cmd.angular.z = angular_speed
            t0 = rospy.Time.now().to_sec()
            while rospy.Time.now().to_sec() - t0 < math.pi / 2.0 / angular_speed:
                pub.publish(cmd)
                rate.sleep()
    cmd.linear.x = 0.0
    cmd.angular.z = 0.0
    pub.publish(cmd)

def handle(req):
    move_square(req.side, req.repetitions)
    return RSquareServResponse(True)

def main():
    global pub
    rospy.init_node("square_server")
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    rospy.Service("/square_server", RSquareServ, handle)
    rospy.spin()

main()
