#!/usr/bin/env python
import rospy
from services_quiz.srv import RSquareServ, RSquareServResponse
from geometry_msgs.msg import Twist



def callback(request):
   sd = request.side
   rp = request.repetitions

   i = 0
   move.linear.x = sd
   move.angular.z = sd
   while i <= rp:
       pub.publish(move)
       i += 1
  
   response = RSquareServResponse()
   response.success = True
   return RSquareServ()

rospy.init_node("right_square_node", anonymous = True)
server = rospy.Service("/rsquare_server", RSquareServ, callback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
move = Twist()
rospy.loginfo("The server is up and running!")
rospy.spin()
