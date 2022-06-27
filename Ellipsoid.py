#! python3
# Ellipsoid.py - Defines equations and functions specific to determining
# whether points on an ellipsoid intersect with a plane

import math

class Ellipsoid(object):
    ELLIPSOID_CENTER_X = 0
    ELLIPSOID_CENTER_Y = 0
    ELLIPSOID_CENTER_Z = 0
    SEMI_X_RADIUS = 0
    SEMI_Y_RADIUS = 0
    SEMI_Z_RADIUS = 0

    def __init__(self, centerX, centerY, centerZ, semiXRadius, semiYRadius, semiZRadius):
        self.ELLIPSOID_CENTER_X = centerX
        self.ELLIPSOID_CENTER_Y = centerY
        self.ELLIPSOID_CENTER_Z = centerZ
        self.SEMI_X_RADIUS = semiXRadius
        self.SEMI_Y_RADIUS = semiYRadius
        self.SEMI_Z_RADIUS = semiZRadius

    def pointOnShape(self, x, y, z):
        #((x-h)/a)^2 + ((y-k)/b)^2 + ((z-l)/c)^2 = 1
        if (((math.pow(((x - self.ELLIPSOID_CENTER_X) / self.SEMI_X_RADIUS), 2)) +
        (math.pow(((y - self.ELLIPSOID_CENTER_Y) / self.SEMI_Y_RADIUS), 2)) +
        (math.pow(((z - self.ELLIPSOID_CENTER_Z) / self.SEMI_Z_RADIUS), 2))) != 1):
            return False
        else:
            return True


