#!usr/bin/env python
import rospy
import math
import random
from std_msgs.msg import *

def ORSBoat():
    msgs = ['rudder/pos','rudder/set_point','sail/pos','sail/set_point','GPS/latitude','GPS/longitude', 'GPS/direction']
    pubs = {}
    for msg in msgs:
        pubs[msg] = rospy.Publisher(msg,Int16,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        for p in pubs.itervalues():
            v = int(random.random()*10)
            p.publish(v)
        rate.sleep()
if __name__ == '__main__':
    try:
        ORSBoat()
    except rospy.ROSInterruptException:
        pass

