import RPi.GPIO as GPIO
from initdist import initdist
from getdist  import getdist
from time import sleep
from robot import Robot
from rmap import RMap
from calculate import find_diff_pos
from calculate import find_diff_angle
from camera import getcamera
from serial import set_l_motor, set_r_motor
from serial import get_sounds


DT = .05

try:
    initdist()
    aibot = Robot()
    rmap = RMap(3.0, 3.0, 20)

    while True:
        sleep(DT)

        #Calculate new position
        change_angle = find_diff_angle(aibot, DT)
        change_pos = find_diff_pos(aibot, change_angle, DT)

        # Get Distance and Camera
        dist  = getdist()
        sounds = getsound()

        #Update map:
        rmap.create_wall(change_pos, change_angle, dist)

        #Determine next controls:
        aibot.update(rmap, dist, sounds[1], sounds[2])

        #Set the robot moving
        set_l_motor(aibot.lmotor)
        set_r_motor(aibot.rmotor)

except KeyboardInterrupt:
    print("Done?")
    sleep(.5)
    set_l_motor(0)
    set_r_motor(0)

    GPIO.cleanup()

