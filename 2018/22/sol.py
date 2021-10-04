#!/usr/bin/python3
import argparse
import re
import heapq
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

with open(args.file, 'r') as f:
    [dp] = map(int, re.findall(r'\d+', f.readline()))
    [tx,ty] = map(int, re.findall(r'\d+', f.readline()))

el = dict()
def region(x,y):
    if (x,y) not in el:
        if y == 0:
            gi = x * 16807
        elif x == 0:
            gi = y * 48271
        elif (x,y) == (tx,ty):
            gi = 0
        else:
            region(x-1,y)
            region(x,y-1)
            gi = el[(x-1,y)] * el[(x,y-1)]
        el[(x,y)] = (gi + dp) % 20183

    return el[(x,y)] % 3

if args.part == 1:
    risk = sum(region(x,y) for y in range(ty + 1) for x in range(tx + 1))
    print(risk)

elif args.part == 2:
    dist = defaultdict(lambda: float('inf'))
    dist[(0,0,0)] = 0

    to_visit = [(0, (0,0,0))]
    visited = set()
    while to_visit:

        _, current = heapq.heappop(to_visit)
        cx,cy,ct = current
        
        if current in visited: continue
        if (cx,cy,ct) == (tx,ty,0): break

        cd = dist[current]
        cr = region(cx,cy)
        nt = (ct + 2*(ct == cr) - 1) % 3

        def update_neigh(neigh, time):
            if (neigh[0] >= 0 and neigh[1] >= 0 and (region(*neigh[:2]) - neigh[2])%3 in (0,2)):
                nd = cd + time
                if nd < dist[neigh]:
                    dist[neigh] = nd
                    heapq.heappush(to_visit, (nd, neigh))

        update_neigh((cx+1,cy,ct), 1)
        update_neigh((cx,cy+1,ct), 1)
        update_neigh((cx-1,cy,ct), 1)
        update_neigh((cx,cy-1,ct), 1)
        update_neigh((cx,cy,nt), 7)

        visited.add((cx,cy,ct))

    print(dist[current])
