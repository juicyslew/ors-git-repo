#!/usr/bin/env python
import rospy
"""
This file reads from:
- heading_err (std_msgs/Int16)

and publishes to:
- auto_mode/rudder/set_point (std_msgs/Int16)

"""

# This line may need to change depending on your message types
from std_msgs.msg import Int16, Float32
import math

class autonomousRudderPublisher:#needs a topic to read in waypoint angle from
	def __init__(self):
		rospy.init_node('rudder_publisher')

		# Step 1: Initialize publishers. This will be referred to later whenever data is transmitted.
		self.rudderPub = rospy.Publisher('auto_mode/rudder/set_point', Int16)

		# Step 2: Initialize subscribers. Each subscriber (incomming information) gets a "self.*" variable, a callback, and a subscriber
		self.waypoint = 0
		self.waypointAngleSub = rospy.Subscriber('heading_err', Int16, self.onAngle)

	def onAngle(msg):
		self.waypoint = msg.data

	def calculateRudderPosition(self, waypointAngle):
		# Do your main logic in a separate function for cleanliness reasons.

		turnAngle = 0
		if abs(waypointAngle) < 90:
			turnAngle = waypointAngle / 2  
		else:
			if(waypointAngle > 0):
				turnAngle = 45
			else:
				turnAngle = -45
		return turnAngle

	def run(self):
		rate = rospy.Rate(10)  # 10hz refresh rate
		while not rospy.is_shutdown():
			rud = self.calculateRudderPosition(self.waypoint)
			
			# This is where the actual publishing happens
			self.rudderPub.publish(rud)

			rate.sleep

	def next_waypoint_rel(location, next_waypoint):
		'''
		CALCULATES THE NEXT RALATAVE DISTAAAANCE.  Uses some rad maths and cool cats to do some lit ass shit.

        Translation:
        calculates the relative distance and angle 
		'''
		#Returns position of next wavepoint relative to boat
		distance = sqrt(	(location.x - next_waypoint.x^2	+ (location.y - next_waypoint.y^2	) #distance calculated
		relangle = math.degrees(math.atan2((location.y - next_waypoint.y),(location.x - next_waypoint.x))) #
		preAngle = relangle - location.theta
		if (preAngle > 180):
			angle = preAngle - 360
		elif(preAngle < -180):
			angle = preAngle + 360
		else:
			angle = preAngle
		return [distance, angle]


if __name__ == '__main__':
	try:
		handler = autonomousRudderPublisher()
		handler.run()
	except rospy.ROSInterruptException:
		pass
