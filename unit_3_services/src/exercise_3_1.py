#! /usr/bin/env python

import rospy, rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest

rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"



rospy.init_node('service_client') 
rospy.wait_for_service('/execute_trajectory') 

move = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
execute_trajectory_request_object = ExecTrajRequest()

execute_trajectory_request_object.file = traj


result = move(execute_trajectory_request_object)

print result


