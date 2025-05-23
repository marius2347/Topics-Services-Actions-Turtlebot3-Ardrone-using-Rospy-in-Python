#!/usr/bin/env python
import rospy
import actionlib
from std_msgs.msg import Empty
from actions_quiz.msg import DroneAction, DroneFeedback, DroneResult

server = None
pub_takeoff = None
pub_land = None
fb_msg = DroneFeedback()
res_msg = DroneResult()

def execute(goal_msg):
    global server
    command = goal_msg.goal
    r = rospy.Rate(1)
    if command == "TAKEOFF":
        pub_takeoff.publish(Empty())
        fb_msg.feedback = "TAKEOFF"
        while not rospy.is_shutdown():
            server.publish_feedback(fb_msg)
            if server.is_preempt_requested():
                server.set_preempted()
                return
            r.sleep()
    elif command == "LAND":
        pub_land.publish(Empty())
        fb_msg.feedback = "LAND"
        for i in range(3):
            if server.is_preempt_requested():
                server.set_preempted()
                return
            server.publish_feedback(fb_msg)
            r.sleep()
        server.set_succeeded(res_msg)

if __name__ == "__main__":
    rospy.init_node("ardrone_action_server_node")
    pub_takeoff = rospy.Publisher("/ardrone/takeoff", Empty, queue_size = 1)
    pub_land = rospy.Publisher("/ardrone/land", Empty, queue_size = 1)
    server = actionlib.SimpleActionServer("ardrone_action_server", DroneAction, execute, False)
    server.start()
    rospy.spin()

