#!/usr/bin/python3
import argparse
from itertools import product

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

points = set()
with open(args.file, 'r') as f:
    for line in f:
        points.add(tuple(map(int, line.split(','))))

def dist(p):
    return sum(map(abs, p))

v = range(-3,4)
near = list(filter(lambda x: 0 < dist(x) < 4, product(v,v,v,v)))

neighbors = {}
for p in points:
    neighbors[p] = set()
    for n in near:
        t = tuple(map(sum, zip(p, n)))
        if t in points:
            neighbors[p].add(t)

if args.part == 1:
    count = 0
    visited = set()
    for p in points:
        if p not in visited:
            count += 1
            to_visit = {p}
            while to_visit:
                cur = to_visit.pop()
                visited.add(cur)
                to_visit.update(filter(lambda x: x not in visited, neighbors[cur]))

    print(count)

elif args.part == 2:
    print('part2')
