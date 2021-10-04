#!/usr/bin/python3
import argparse
import re
import math
import heapq

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

p = re.compile(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")

nanobots = dict()
with open(args.file, 'r') as f:
    for line in f:
        m = p.match(line)
        x,y,z,r = map(int, m.groups())
        nanobots[(x,y,z)] = r

if args.part == 1:
    bestr, (sx,sy,sz) = max((r,xyz) for xyz,r in nanobots.items())
    count = sum(abs(x-sx) + abs(y-sy) + abs(z-sz) <= bestr for x,y,z in nanobots)
    print(count)

elif args.part == 2:
    maxsize = max(max(map(abs, xyz))+r for xyz,r in nanobots.items())
    maxsize = 2**math.ceil(math.log2(maxsize))

    def intersects(box, bot):
        d = 0
        for bl, bh, v in zip(box[0], box[1], bot):
            d += abs(v - bl) + abs(v - bh) - (bh - bl)

        return d <= 2*nanobots[bot] 
    
    box = ((-maxsize,)*3, (maxsize-1,)*3)
    tocheck = [(-len(nanobots), -2*maxsize, 3*maxsize, box)]
    while tocheck:
        (count, size, dist, box) = heapq.heappop(tocheck)
        if size == -1: break

        size = size // -2
        for octant in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
            botcorner = tuple(v + size * o for v, o in zip(box[0], octant))
            topcorner = tuple(v + size - 1 for v in botcorner)
            newbox = (botcorner, topcorner)
            count = sum(intersects(newbox, b) for b in nanobots)
            heapq.heappush(tocheck, (-count, -size, sum(map(abs, botcorner)), newbox))
        
    print(dist)
