import RPi.GPIO as GPIO
from initdist import initdist
from getdist  import getdist
from time import sleep

try:
    initdist()

    while True:
        print getdist()
        sleep(.1)

except KeyboardInterrupt:
    print("Done?")
    GPIO.cleanup()

