from CALCULATE_SETTINGS import *

def sound_calc_motors(sounds):
    ls = sounds[0]
    rs = sounds[1]

    # Drive left
    if ls - rs > TOLERANCE:
        return (BASE_SPEED + rs * NS, BASE_SPEED + ls * NS)


    # Drive right
    if rs - ls > TOLERANCE:
        return (BASE_SPEED + rs * NS, BASE_SPEED + ls * NS)
