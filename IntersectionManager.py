#! python3
# intersectionManager.py - Handles high-level intersection finding behavior

from IntersectionFinder import IntersectionFinder

MAX_X = 0
MAX_Y = 0
MAX_Z = 0
X_PLANE = 0

progRunning = True
while progRunning:
    print('Enter the max x-axis value: ', end = '')
    MAX_X = int(input())
    print('Enter the max y-axis value: ', end = '')
    MAX_Y = int(input())
    print('Enter the max z-axis value: ', end = '')
    MAX_Z = int(input())
    print('Using plane x = ', end = '')
    X_PLANE = int(input())

    finder = IntersectionFinder(MAX_X, MAX_Y, MAX_Z, X_PLANE)
    print(finder.find())
    print('Continue running program? ', end = '')
    decision = str(input())
    if decision != 'Y':
        progRunning = False

print('Goodbye')
