import RPi.GPIO as GPIO
from initdist import initdist
from getdist  import getdist
from time import sleep
from robot import Robot
from rmap import RMap
from calculate import sound_calc_motors
from camera import getcamera
from serial import set_l_motor, set_r_motor
from serial import get_sounds
from RUNSETTINGS import *


def chase_tail(aibot, dist, lastdist):
    SPIN = SPIN_SPEED
    for i in range(0,10):
        if dist < lastdist:
            set_l_motor(CHASE_SPEED)
            set_l_motor(CHASE_SPEED)
            for i in range(0,5):
                sleep(DT)
        if dist > lastdist:
            for i in range(0,6):
                if i == 2:
                    SPIN = - SPIN

                set_l_motor(SPIN)
                set_r_motor(-SPIN)

                sleep(DT/1.4)
                lastdist = dist
                dist = getdist()

                if (dist < lastdist):
                    break

def detect_area(aibot):
    dist_list = []
    set_l_motor(DETECT_SPEED)
    set_r_motor(-DETECT_SPEED)
    #DETECT_SPEED = -DETECT_SPEED

    for i in range(0,20):
        dist_list.append(getdist())
        if dist > LONG_RANGE:
            return;

        sleep(DT)

try:
    initdist()
    aibot = Robot()
    detected_area = False
    dist = getdist()
    lastdist = getdist()

    while True:
        lastdist = dist

        #Set the robot moving
        set_l_motor(aibot.lmotor)
        set_r_motor(aibot.rmotor)

        sleep(DT)

        # Get Distance and Camera
        dist  = getdist()
        diff = dist - lastdist

        if (abs(diff) >  THRESHOLD):
            if (lastdist < MAX or dist < MAX):
                detected_area = False
                aibot.movequeue = []
                chase_tail(aibot, dist, lastdist)
                continue

        if (len(aibot.movequeue) != 0):
            aibot.execute_queue()
            continue;

        if (dist < WALLDIST):
            detected_area = False
            aibot.wall_react()
            continue;
        """
        if sounds != (0.0, 0.0):
            lr_motors = sound_calc_motors(sounds)
            lmot = lr_motors[0]
            rmot = lr_motors[1]

            aibot.lmotor = lmot[0]
            aibot.rmotor = rmot[1]

            if (lmot == rmot):
                for i in range(0, 20):
                    aibot.movequeue.append((lmot, rmot)):


            for i in range(0,3):
                aibot.movequeue.append((lmot, rmot))
            continue;
        """

        if not detected_area:
            detect_area(aibot)
            detected_area = True

        aibot.navigate()

except KeyboardInterrupt:
    print("Done?")
    sleep(.5)
    set_l_motor(0)
    set_r_motor(0)

    GPIO.cleanup()

