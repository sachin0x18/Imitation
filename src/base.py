#!/usr/bin/python

################################################################################

# Code for sending remote motion commands to the robot (e. forward,backward)

################################################################################

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import sys, select, termios, tty

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__=="__main__":
    rospy.init_node('base',anonymous=True)
    settings = termios.tcgetattr(sys.stdin)
    pub = rospy.Publisher('command', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            key = getKey()
            pub.publish(key)
            rate.sleep()
        except:
            continue
#    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
