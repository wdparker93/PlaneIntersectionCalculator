#! python3
# Sphere.py - Defines equations and functions specific to determining
# whether points on a sphere intersect with a plane

import math

class Sphere(object):
    SPHERE_CENTER_X = 0
    SPHERE_CENTER_Y = 0
    SPHERE_CENTER_Z = 0
    SPHERE_RADIUS = 0

    def __init__(self, centerX, centerY, centerZ, radius):
        self.SPHERE_CENTER_X = centerX
        self.SPHERE_CENTER_Y = centerY
        self.SPHERE_CENTER_Z = centerZ
        self.SPHERE_RADIUS = radius

    def pointOnShape(self, x, y, z):
        #(x-a)^2 + (y-b)^2 + (z-c)^2= r^2
        if (math.pow((x - self.SPHERE_CENTER_X), 2) + math.pow((y - self.SPHERE_CENTER_Y), 2) +
        math.pow((z - self.SPHERE_CENTER_Z), 2) != math.pow(self.SPHERE_RADIUS, 2)):
            return False
        else:
            return True
