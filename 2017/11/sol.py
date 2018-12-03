#!/usr/bin/python3
import argparse
from math import sqrt

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
    
moves = []

with open(args.file, 'r') as f:
    moves = f.read().strip('\n').split(',')
    
x = y = z = 0

maxdist = 0
dist = 0

for m in moves:
    if m == 'n':
        y += 1
        z -= 1
    elif m == 'ne':
        x += 1
        z -= 1
    elif m == 'se':
        x += 1
        y -= 1
    elif m == 's':
        y -= 1
        z += 1
    elif m == 'sw':
        x -= 1
        z += 1
    elif m == 'nw':
        x -= 1
        y += 1
    
    dist = max(abs(x), abs(y), abs(z))
    if dist > maxdist:
        maxdist = dist
            
if args.part == 1:       
    print(dist)

if args.part == 2:
    print(maxdist)
