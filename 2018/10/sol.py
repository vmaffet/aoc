#!/usr/bin/python3
import argparse
import re
import numpy as np
from matplotlib import pyplot as plt
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

starInfo = dict()      
starPose = defaultdict(lambda:[], dict())

minX, maxX, minY, maxY = 0, 0, 0, 0

count = 0
with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match('position=<([ -]?\d+), ([ -]?\d+)> velocity=<([ -]?\d+), ([ -]?\d+)>', line)
        if matcher:
            x, y, vx, vy = list(map(int, matcher.groups()))
            starInfo[count] = (vx, vy)
            starPose[(x, y)].append(count)
            count += 1


def computeMinMax():
    mX, MX, mY, MY = float('inf'), float('-inf'), float('inf'), float('-inf')
    for x, y in starPose:
        mX = min(mX, x)
        MX = max(MX, x)
        mY = min(mY, y)
        MY = max(MY, y)
    return (mX, MX, mY, MY) 


def showSky():
    img = np.zeros((maxY-minY+1, maxX-minX+1), dtype=bool)
    for star in starPose:
        x, y = star
        img[y-minY, x-minX] = 1
    plt.imshow(img, interpolation = 'nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()


def doStep():
    newPose = defaultdict(lambda:[], dict())
    for star in starPose:
        x, y = star
        for id in starPose[star]:
            vx, vy = starInfo[id]
            nx, ny = x+vx, y+vy
            newPose[(nx, ny)].append(id)
    return newPose

    
def noSymbol():
    for curx, cury in starPose:
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                count += 1 if (curx+i, cury+j) in starPose else 0
        if count == 1:
            return True
    return False

seconds = 0
while noSymbol():
    seconds += 1
    starPose = doStep()

minX, maxX, minY, maxY = computeMinMax()
showSky()

print(seconds)
