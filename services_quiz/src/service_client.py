#!/usr/bin/env python
import rospy
from services_quiz.srv import RSquareServ, RSquareServRequest

def main():
    rospy.init_node("square_client")
    rospy.wait_for_service("/square_server")
    call = rospy.ServiceProxy("/square_server", RSquareServ)
    req = RSquareServRequest(side = 1.0, repetitions = 2)
    resp = call(req)
    if resp.success:
        rospy.loginfo("S-a terminat miscarea!")
    else:
        rospy.logwarn("Inca nu s-a terminat!")

main()
