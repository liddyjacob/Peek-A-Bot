from camera_ai import findEnemy
from ROBOT_SETTINGS import *

"""

The robot class contains several parameters.

The angle parameter is based off a unit circle,

   90
   _<_
  /   \
-|--+--| 0
  \   /
   ->-

Counter clockwise: Left is up
"""



class Robot:
    def __init__(self):
        self.lmotorpwr = 0 # Max 255 power
        self.rmotorpwr = 0 # Max 255 power
        self.pos = (0.0, 0.0)
        self.angle = 0.0
        self.angle_goal = 0.0

        print "Robot initialization"

    def update(self, rmap, dist, frame):
        if (dist < 10):
            self.lmotorpower = -50
            self.rmotorpower = -50
            print("WOAH! Back up boi!")

        else:
            diffangle = findEnemy(frame)
            self.angle_goal = diffangle + self.angle
            self.calculate_motors()

    def calculate_motors(self):
        # Tolerance makes sure the robot will not adjust for minor diff
        if ((self.angle_goal + TOLERANCE) % 360) > (self.angle % 360 ):
            # Go left:
            self.lmotor = 255
            self.rmotor = -255
        elif ((self.angle_goal - TOLERANCE) % 360)  <  (self.angle % 360):
            # Go right:
            self.lmotor = -255
            self.rmotor = 255
        else:
            self.lmotor = 128
            self.rmotor = 128
