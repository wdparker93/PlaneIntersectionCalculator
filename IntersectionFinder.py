#! python3
# IntersectionFinder.py - Determines the points where a plane and 3D shape intersect, if any

import math, os
from shapes.Sphere import Sphere
from shapes.Torus import Torus
from shapes.Ellipsoid import Ellipsoid
from sys import path

class IntersectionFinder(object):
    X_LIMIT = 0
    Y_LIMIT = 0
    Z_LIMIT = 0

    PLANE_A = 0
    PLANE_B = 0
    PLANE_C = 0
    PLANE_D = 0

    def __init__(self, maxX, maxY, maxZ, xPlane):
        self.X_LIMIT = maxX
        self.Y_LIMIT = maxY
        self.Z_LIMIT = maxZ
        self.PLANE_A = 1
        self.PLANE_D = xPlane

    def pointOnPlane(self, x, y, z):
        #Ax + By + Cz = D
        #Plane is x = 4 where z = 0 to Z_LIMIT and y  0 to Y_LIMIT
        if ((self.PLANE_A * x) + (self.PLANE_B * y) + (self.PLANE_C * z) != self.PLANE_D):
            return False
        else:
            return True

    def pointOnShape(self, shape, x, y, z):
        return shape.pointOnShape(x, y, z)

    def getIntersectionPoints(self, shape):
        intersectionPoints = {}
        dictCounter = 0
        for i in range(1, self.X_LIMIT, 1):
            for j in range(1, self.Y_LIMIT, 1):
                for k in range(1, self.Z_LIMIT, 1):
                    if self.pointOnShape(shape, i, j, k):
                        if self.pointOnPlane(i, j, k):
                            intersectionPoints[dictCounter] = [i, j, k]
                            dictCounter += 1
        return intersectionPoints

    def printIntersection(self, intersectionPoints):
        gridToPrint = {}
        maxHeight = int(self.maxIntersectionHeight(intersectionPoints))
        for i in range(1, self.Z_LIMIT - (maxHeight - 1), 1):
            for j in range(1, self.Y_LIMIT, 1):
                gridToPrint[j, i] = '.'
        for i in range(self.Z_LIMIT - maxHeight, self.Z_LIMIT, 1):
            for j in range(1, self.Y_LIMIT, 1):
                gridToPrint[j, i] = '.'
                for value in intersectionPoints.values():
                    yValue = value[1]
                    zValue = self.Z_LIMIT - value[2]
                    if (yValue == j and zValue == i):
                        gridToPrint[j, i] = 'x'
        for i in range(1, self.Z_LIMIT, 1):
            for j in range(1, self.Y_LIMIT, 1):
                print(gridToPrint[j, i], end = ' ')
            print()

    def maxIntersectionHeight(self, intersectionPoints):
        maxHeight = 0;
        for value in intersectionPoints.values():
            if value[2] > maxHeight:
                maxHeight = value[2]
        return maxHeight

    def minIntersectionHeight(self, intersectionPoints):
        minHeight = self.Z_LIMIT
        for value in intersectionPoints.values():
            if value[2] < minHeight:
                minHeight = value[2]
        return minHeight

    def buildShape(self, shape):
        print('Enter x-coordinate of center: ', end = '')
        centerX = int(input())
        print('Enter y-coordinate of center: ', end = '')
        centerY = int(input())
        print('Enter z-coordinate of center: ', end = '')
        centerZ = int(input())

        if shape == 'SPHERE':
            print('Enter radius: ', end = '')
            radius = int(input())
            shape = Sphere(centerX, centerY, centerZ, radius)
        elif shape == 'TORUS':
            print('Enter distance from center of hole to center of tube: ', end = '')
            holeToMidTube = int(input())
            print('Enter radius of tube: ', end = '')
            tubeRadius = int(input())
            shape = Torus(centerX, centerY, centerZ, holeToMidTube, tubeRadius)
        elif shape == 'ELLIPSOID':
            print('Enter length of semi x-axis: ', end = '')
            semiXAxis = int(input())
            print('Enter length of semi y-axis: ', end = '')
            semiYAxis = int(input())
            print('Enter length of semi z-axis: ', end = '')
            semiZAxis = int(input())
            shape = Ellipsoid(centerX, centerY, centerZ, semiXAxis, semiYAxis, semiZAxis)

        return shape

    def find(self):
        print('Please specify a shape: ', end = '')
        shape = self.buildShape(str(input()).upper())
        intersectionPoints = self.getIntersectionPoints(shape)
        self.printIntersection(intersectionPoints)
        top = self.maxIntersectionHeight(intersectionPoints)
        bottom = self.minIntersectionHeight(intersectionPoints)
        topBottom = [top, bottom]
        return topBottom

