import os
from time import sleep

LADJ = 1
RADJ = .92
#screen must be running

def set_l_motor(lval):
    lval = (lval * LADJ)
    os.system("echo '<L," + str(lval) + ">' | tee /dev/ttyACM0")

def set_r_motor(rval):
    rval = int(rval * RADJ)
    os.system("echo '<R," + str(rval) + ">' | tee /dev/ttyACM0")

def meow(robot):
    set_l_motor(0)
    set_r_motor(0)
    os.system("echo '<M,0>' | tee /dev/ttyACM0")
    sleep(2.1)
    set_l_motor(robot.lmotor)
    set_r_motor(robot.rmotor)


# Write to $dmesg | grep ttyS

