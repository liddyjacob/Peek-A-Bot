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
        self.lmotor = 0 # Max 255 power
        self.rmotor = 0 # Max 255 power
        self.pos = (0.0, 0.0)
        self.angle = 0.0
        self.change_angle = 0.0
        self.movequeue = []

        print "Robot initialization"

    def update(self, rmap, dist, lsound, rsound):



        if len(self.movequeue) != 0:
            lr = self.movequeue.pop()
            self.lmotor = lr[0]
            self.rmotor = lr[1]
            return

        if (dist < 20):
            for i in range(0,15):
                self.movequeue.insert(0,(-150, -150))

            for i in range(0,5):
                self.movequeue.insert(0,(230, -230))

        else:
            self.change_angle = findEnemy(frame)
            self.calculate_motors()

    def calculate_motors(self):
        # Tolerance makes sure the robot will not adjust for minor diff
        if self.change_angle > TOLERANCE:
            # Go left:
            self.lmotor = -255
            self.rmotor = 255
        elif self.change_angle < -TOLERANCE:
            # Go right:
            self.lmotor = 255
            self.rmotor = -255
        else:
            # Go straight
            self.lmotor = 200
            self.rmotor = 200

