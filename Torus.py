#! python3
# Torus.py - Defines equations and functions specific to determining
# whether points on a torus intersect with a plane

import math

class Torus(object):
    HOLE_CENTER_X = 0
    HOLE_CENTER_Y = 0
    HOLE_CENTER_Z = 0
    HOLE_TO_MID_TUBE = 0
    TUBE_RADIUS = 0

    def __init__(self, centerX, centerY, centerZ, holeToMidTube, tubeRadius):
        self.HOLE_CENTER_X = centerX
        self.HOLE_CENTER_Y = centerY
        self.HOLE_CENTER_Z = centerZ
        self.HOLE_TO_MID_TUBE = holeToMidTube
        self.TUBE_RADIUS = tubeRadius

    def pointOnShape(self, x, y, z):
        #(c - sqrt(x^2 - y^2))^2 + z^2 = a^2
        if ((math.pow((self.HOLE_TO_MID_TUBE -
        math.sqrt(math.pow(x - self.HOLE_CENTER_X, 2) + math.pow(y - self.HOLE_CENTER_Y, 2))), 2) +
        math.pow(z - self.HOLE_CENTER_Z, 2))
        != math.pow(self.TUBE_RADIUS, 2)):
            return False
        else:
            return True
