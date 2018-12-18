#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

network = []
        
with open(args.file, 'r') as f:
    for line in f:
        if line.strip():
            network.append(list(line.strip('\n')))
        
carts = []

for y in range(len(network)):
    for x in range(len(network[y])):
        if network[y][x] in '>^<v':
            carts.append([x, y, network[y][x], 0])

def movecarts(wagons):
    poses = dict()
    wagons = sorted(wagons, key=lambda w : (w[1], w[0]))
    for i in range(len(wagons)):
        x, y, d, t = wagons[i]
        if (x, y) in poses:
            poses[(x, y)].append(i)
            continue
        if d is '>':
            x += 1
        elif d is '^':
            y -= 1
        elif d is '<':
            x -= 1
        elif d is 'v':
            y += 1
        r = network[y][x]
        if (x, y) in poses:
            poses[(x, y)].append(i)
            continue
        if r is '/':
            if d is '>':
                d = '^'
            elif d is '^':
                d = '>'
            elif d is '<':
                d = 'v'
            elif d is 'v':
                d = '<'
        elif r is '\\':
            if d is '>':
                d = 'v'
            elif d is '^':
                d = '<'
            elif d is '<':
                d = '^'
            elif d is 'v':
                d = '>'
        elif r is '+':
            if (d is '>' and t is 0) or (d is '<' and t is 2):
                d = '^'
            elif (d is 'v' and t is 0) or (d is '^' and t is 2):
                d = '>'
            elif (d is '<' and t is 0) or (d is '>' and t is 2):
                d = 'v'
            elif (d is '^' and t is 0) or (d is 'v' and t is 2):
                d = '<'
            t = (t+1) % 3
        wagons[i] = (x, y, d, t)
        poses[(x, y)] = [i]
    
    topop = []
    ok = True
    pose = None
    for k, v in poses.items():
        if len(v) > 1:
            ok = False
            topop.extend(v)
            pose = k
            
    for x in reversed(topop):
        wagons.pop(x)
    
    return wagons, ok, pose
        

if args.part == 1:
    ok = True
    while ok:
        carts, ok, pose = movecarts(carts)
        
    print('{},{}'.format(pose[0], pose[1]))

elif args.part == 2:
    while len(carts) > 1:
        carts, ok, pose = movecarts(carts)
        
    print('{},{}'.format(carts[0][0], carts[0][1]))
