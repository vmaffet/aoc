#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

positions = []
maxX = maxY = 0
with open(args.file, 'r') as f:
    for line in f:
        if line.strip():
            pos = tuple(map(int, line.split(', ')))
            positions.append(pos)
            maxX = max(maxX, pos[0])
            maxY = max(maxY, pos[1])

if args.part == 1:
    parcel_count = [ 0 for i in range(len(positions)) ]
    distances = [ 0 for i in range(len(positions)) ]
    for y in range(maxY+1):
        for x in range(maxX+1):
            for i in range(len(positions)):
                distances[i] = abs(x-positions[i][0]) + abs(y-positions[i][1])
            if distances.count(min(distances)) == 1:
                loc = distances.index(min(distances))
                if x == 0 or x == maxX or y == 0 or y == maxY:
                    parcel_count[loc] = float('-inf')
                else:
                    parcel_count[loc] += 1
    print(max(parcel_count))
   
elif args.part == 2:
    limit = 10000
    safe_count = 0
    for y in range(maxY+1):
        for x in range(maxX+1):
            dist_sum = 0
            for i in range(len(positions)):
                dist_sum += abs(x-positions[i][0]) + abs(y-positions[i][1])
            safe_count += 1 if dist_sum < limit else 0
    print(safe_count)
