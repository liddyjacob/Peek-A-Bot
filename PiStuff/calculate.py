from CALCULATE_SETTINGS import *

def ROC_angle_motors(lmotor, rmotor):
    return rmotor - lmotor # Some function resembling this: maybe log

def RADIUS_motors(lmotor, rmotor):
    return 1.0 / (abs(rmotor + lmotor) - 500) # Some function from this type

def find_diff_angle(bot, time):
    return ROC_angle_motors(bot.lmotor, bot.rmotor) * (time)
    pass
    #print "Finding new pos"

# Assume robot is going in circle: Use trig.
def find_diff_pos(bot, DTheta, time):

    # Radius is a function of
    r = RADIUS_motors(bot.lmotor, bot.rmotor)

    # Calculate angle for tangent
    DPTheta = DTheta - 90
    # cot (DPT) = x' / y'
    #  => x' = cot(DPT) y'
    # x^2 + y^2 = r^2
    #  => x = sqrt(r^2 - y^2)

    return (0, 0)
    pass
    #print "Finding new pos"
