
class RMap:
    def __init__(self, length, height, grain):
        self.length = length
        self.height = height
        self.grain = grain # How many points per sq meter.
        self.create_map()

    def create_map(self):
        ival = int(-self.length * self.grain / 2)
        jval = int(-self.height * self.grain / 2)
        for i in range(-ival, ival + 1):
            for j in range(-jval, jval):
                print i, j

    def create_wall(self, pos, angle, dist):
        pass
        #print pos
        #print angle
        #print dist

#def dist_from_line
