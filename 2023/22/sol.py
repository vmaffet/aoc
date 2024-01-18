#!/usr/bin/python3

from collections import defaultdict, namedtuple
import re

Point = namedtuple('Point', ['x', 'y', 'z'])

snapshot = []
with open('input.txt', 'r') as f:
    for line in f:
        x0,y0,z0, x1,y1,z1 = map(int, re.findall(r'\d+', line))
        snapshot.append((Point(x0,y0,z0), Point(x1,y1,z1)))

def cross(brickA, brickB):
    overlapX = brickA[0].x <= brickB[1].x and brickA[1].x >= brickB[0].x
    overlapY = brickA[0].y <= brickB[1].y and brickA[1].y >= brickB[0].y
    return overlapX and overlapY

stack = []
for bA in sorted(snapshot, key=lambda b: b[0].z):
    maxZ = 0
    for bB in stack:
        if cross(bA, bB):
            maxZ = max(maxZ, bB[1].z)
    
    x0,y0, x1,y1 = bA[0].x,bA[0].y, bA[1].x,bA[1].y
    z0, z1 = maxZ+1,maxZ+1+bA[1].z-bA[0].z
    stack.append((Point(x0,y0,z0), Point(x1,y1,z1)))

supports = defaultdict(set)
supportedBy = defaultdict(set)
for i, bA in enumerate(stack):
    for j, bB in enumerate(stack):
        if cross(bA, bB) and bA[1].z + 1 == bB[0].z:
            supports[i].add(j)
            supportedBy[j].add(i)

# ==== Part 1 ==== #
loadBearing = {v.pop() for v in supportedBy.values() if len(v) == 1}
print(len(stack) - len(loadBearing))

# ==== Part 2 ==== #
res = 0
for i in supports:

    fallen = {i}
    queue = list(supports[i])
    while queue:
        j = queue.pop(0)
        if all(x in fallen for x in supportedBy[j]):
            fallen.add(j)
            if j in supports:
                queue.extend(list(supports[j]))

    res += len(fallen) - 1

print(res)