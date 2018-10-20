class Robot:
    def __init__(self):
        self.lmotorpwr = 0 # Max 255 power
        self.rmotorpwr = 0 # Max 255 power
        self.pos = (0.0, 0.0)
        self.angle = 0.0

        print "Robot initialization"

    def update(self, rmap, dist, frame):
        if (dist < 10):
            print("WOAH! Back up boi!")
        #print "Update"
