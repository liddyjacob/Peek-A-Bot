import RPi.GPIO as GPIO
import time

#GPIO_TRIGGER and GPIO_ECHO
from gpiosettings import *

def initdist():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
