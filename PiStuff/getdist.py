import RPi.GPIO as GPIO
from time import time
from time import sleep
#GPIO_(TRIGGER, ECHO)
from gpiosettings import *

def getdist():
    # Shoot!
    GPIO.output(GPIO_TRIGGER, True)

    # Wait!
    sleep(.00001)

    # Recieve!
    GPIO.output(GPIO_TRIGGER, False)

    initT = stopT = time()

    while GPIO.input(GPIO_ECHO) == 0:
        initT = time()

    while GPIO.input(GPIO_ECHO) == 1:
        stopT = time()

    # Time elapsed
    interval = stopT - initT

    # Calculate Distance: Change units to CM
    cm_distance = interval * S_TO_CM
    return cm_distance
