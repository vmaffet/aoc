#!/usr/bin/python3
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
        
with open(args.file, 'r') as f:
    serial = int(f.read().strip())
       
width, height = 300, 300
       
powerlevels = np.zeros((width, height))
for x in range(width):
    for y in range(height):
        rackid = x + 11
        powerlevel = ((((rackid * (y+1) + serial) * rackid ) % 1000 ) // 100 ) - 5
        powerlevels[x, y] = powerlevel

bestPower = list()
bestLoc = list()

for s in range(1, min(width, height)):
    patchW, patchH = s, s
    gridpower = np.zeros((width-patchW+1, height-patchH+1))
    for x in range(width-patchW+1):
        for y in range(height-patchH+1):
            gridpower[x, y] = np.sum(powerlevels[x:x+patchW,y:y+patchH])
    bestPower.append(np.max(gridpower))
    bestLoc.append(np.unravel_index(np.argmax(gridpower, axis=None), gridpower.shape))
    

if args.part == 1:
    x, y = bestLoc[2]
    print('{},{}'.format(x+1, y+1))

elif args.part == 2:
    size = bestPower.index(max(bestPower))
    x, y = bestLoc[size]
    print('{},{},{}'.format(x+1, y+1, size+1))
