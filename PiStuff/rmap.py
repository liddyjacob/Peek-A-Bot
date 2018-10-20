
class RMap:
    def __init__(self, length, height, grain):
        self.length = length
        self.height = height
        self.grain = grain # How many points per sq meter.
        self.create_map()

    def create_map(self):
        for i in range(int(-self.length/2), int(self.length/2 + 1)):
            for j in range(int(-self.height/2), int(self.height/2)):
                print i, j

    def create_wall(self, pos, angle, dist):
        print pos
        print angle
        print dist

#def dist_from_line
