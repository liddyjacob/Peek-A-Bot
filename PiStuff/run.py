import RPi.GPIO as GPIO
from initdist import initdist
from getdist  import getdist
from time import sleep
from robot import Robot
from rmap import RMap
from calculate import sound_calc_motors
from camera import getcamera
from serial import set_l_motor, set_r_motor
from serial import meow
from RUNSETTINGS import *
from random import randint

def chase_tail(aibot, dist, lastdist):

    SPIN = SPIN_SPEED
    if randint(0,2): SPIN = -SPIN

    for i in range(0,10):
        if dist < lastdist:
            set_l_motor(CHASE)
            set_l_motor(CHASE)
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


def follow_slowly(aibot):
    entertained = 35
    run_cooldown = 0

    CHASE_TURN = CHASE_SPEED
    DETECT_TURN = DETECT_SPEED

    for i in range(0,300):
        if randint(0,2): CHASE_TURN = -CHASE_TURN
        if randint(0,2): DETECT_TURN = -DETECT_TURN


        if entertained == 0: return

        sleep(DT)
        dist = getdist()

        if run_cooldown > 0:
            set_l_motor(CHASE_SPEED)
            set_r_motor(CHASE_SPEED)
            run_cooldown -= 1
            continue


        if dist < PLAY_DIST:
            entertained-=5
            set_l_motor(0)
            set_r_motor(0)
            meow(aibot)
            continue

        if dist < MAX:
            run_cooldown += 4
            if run_cooldown > 20: run_cooldown = 20
            entertained = 35
            set_l_motor(CHASE_SPEED)
            set_r_motor(CHASE_SPEED)
            continue

        if dist > MAX:

            entertained = 45

            for i in range(0,6):
                entertained-=1
                dist = getdist()
                set_l_motor(DETECT_TURN)
                set_r_motor(-DETECT_TURN)
                if dist < MAX:
                    break

                sleep(DT/2)


            if dist >= MAX:
                set_l_motor(0)
                set_r_motor(0)
                sleep(DT)
                sleep(DT)
                sleep(DT)

                for i in range(0,14):
                    entertained-=1
                    dist = getdist()

                    set_l_motor(-DETECT_TURN)
                    set_r_motor(DETECT_TURN)
                    if dist < MAX:
                        break

                    sleep(DT/2)

            if dist >= MAX:
                set_l_motor(0)
                set_r_motor(0)
                sleep(DT)
                sleep(DT)
                sleep(DT)

                for i in range(0,8):
                    entertained-=1
                    dist = getdist()
                    set_l_motor(DETECT_TURN)
                    set_r_motor(-DETECT_TURN)
                    if dist < MAX:
                        break

                    sleep(DT/2)

                set_l_motor(CHASE_SPEED * .85)
                set_r_motor(CHASE_SPEED * .85)
                for i in range(0,20):
                    dist = getdist()
                    entertained-=.5
                    if dist < MAX:
                        break
                    sleep(DT)







def detect_area(aibot):
    #meow(aibot)
    DETECT_TURN = DETECT_SPEED

    if randint(0,2): DETECT_TURN = -DETECT_TURN
    dist_list = []
    set_l_motor(DETECT_TURN)
    set_r_motor(-DETECT_TURN)
    #DETECT = -DETECT

    maximum = 0
    second = 0
    for i in range(0,34):
        d = getdist()
        dist_list.append(d)
        if d > LONG_RANGE:
            return;

        if d > maximum:
            second = maximum
            maximum = d

        sleep(DT/4)

    for i in range(0,8):
        d = getdist()
        if d >= second * .9: return;
        sleep(DT)

    set_l_motor(0)
    set_r_motor(0)



#if True:
try:
    initdist()
    aibot = Robot()
    detected_area = False
    dist = getdist()
    lastdist = getdist()
    entertained = 40

    follow_slowly(aibot)

    while True:

        lastdist = dist

        #Set the robot moving
        set_l_motor(aibot.lmotor)
        set_r_motor(aibot.rmotor)

        sleep(DT)

        # Get Distance
        dist  = getdist()
        diff = dist - lastdist
        """
        if (abs(diff) >  THRESHOLD):
            if (lastdist < MAX or dist < MAX):
                detected_area = False
                aibot.movequeue = []
                chase_tail(aibot, dist, lastdist)
                continue
        """

        if (len(aibot.movequeue) != 0):
            aibot.execute_queue()
            continue;

        if (dist < WALLDIST):
            entertained = 45
            meow(aibot)
            detected_area = True
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
            entertained = 70
            detect_area(aibot)
            detected_area = True

        aibot.navigate()
        entertained -= 1

        if (entertained == 0):
            follow_slowly(aibot)
            detected_area = False;

except KeyboardInterrupt:
    print("Done?")
    sleep(.5)
    set_l_motor(0)
    set_r_motor(0)

    GPIO.cleanup()

