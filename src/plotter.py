#!/usr/bin/python
################################################################################

# Code for plotting the path traversed.

################################################################################

import rospy
import matplotlib.pyplot as plt
from std_msgs.msg import Float32MultiArray

forward_distance = 0.0
right_distance = 0.0

def callback(data):     
    forward_distance = data.data[0]
    right_distance = data.data[1]
    print("X: "+ str(forward_distance)),
    print("Y: "+ str(right_distance))
    plt.scatter(right_distance,forward_distance)
    plt.plot(right_distance,forward_distance)
    #plt.axis([0, 15, 0, 15])
    plt.draw()
    plt.pause(0.0001)
 
if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True) 
    rospy.Subscriber("distance", Float32MultiArray, callback)
    plt.ion()
    plt.show(block=True) 
    rospy.spin()