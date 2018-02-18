#!/usr/bin/python

################################################################################

# Test code for calulating angles between different body parts

################################################################################
import roslib
roslib.load_manifest('skeleton')
import rospy
import tf
from tf.transformations import *
import numpy as np
import time

def get_xaxis(body_part):
    trans, rot = listener.lookupTransform('/openni_depth_frame',str(body_part),rospy.Duration(0))
    q1 = rot
    q2 = [1,0,0,0]
    return quaternion_multiply(quaternion_multiply(q1, q2), quaternion_conjugate(q1) )[:3]    #inside tf.transformations

def get_angle(v1,v2):
    angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    return angle

if __name__ == '__main__':
    rospy.init_node('kinect_listener',anonymous=True)
    listener = tf.TransformListener()
    while not rospy.is_shutdown():
         try:
             right_shoulder_x = get_xaxis('/right_shoulder_1')
             right_elbow_x = get_xaxis('/right_elbow_1')
             print("Right_shoulder X: "+str(right_shoulder_x))
             print("Right_elbow X: "+ str(right_elbow_x))
             print("Angle between: " + str(get_angle(right_shoulder_x,right_elbow_x)*180/np.pi))
             time.sleep(0.5)
         except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
              continue
