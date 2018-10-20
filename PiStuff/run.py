import RPi.GPIO as GPIO
from initdist import initdist
from getdist  import getdist
from time import sleep
from robot import Robot
from rmap import RMap
from calculate import find_new_pos
from calculate import find_new_angle
from camera import getcamera


try:
    initdist()
    aibot = Robot()
    rmap = RMap(3.0, 3.0, 20)

    while True:
        sleep(.03)

        #Calculate new position:
        newpos = find_new_pos(aibot)
        newangle = find_new_angle(aibot)

        # Get Distance and Camera
        dist  = getdist()
        frame = getcamera()

        #Update map:
        rmap.create_wall(newpos, newangle, dist)

        #Determine next controls:
        aibot.update(rmap, dist, frame)

except KeyboardInterrupt:
    print("Done?")
    GPIO.cleanup()

