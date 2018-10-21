import os


#screen must be running

def set_l_motor(lval):
    os.system("echo '<L," + str(lval) + ">' | tee /dev/ttyACM0")

def set_r_motor(rval):
    os.system("echo '<R," + str(rval) + ">' | tee /dev/ttyACM0")

def get_sounds():
    sounds = os.popen('cat /dev/ttyACM0').read()
    print sounds
    return (0,0)

# Write to $dmesg | grep ttyS

