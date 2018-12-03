#!/usr/bin/python3
import argparse
import difflib
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

n = 1000
cloth = [[0 for i in range(n)] for j in range(n)]

countoverlap = 0
total_nums = set()
bad_nums = set()

with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)
        if matcher:
            num = int(matcher.group(1))
            x = int(matcher.group(2))
            y = int(matcher.group(3))
            w = int(matcher.group(4))
            h = int(matcher.group(5))
            
            total_nums.add(num)
            for i in range(w):
                for j in range(h):
                    if cloth[x+i][y+j] == 0:
                        cloth[x+i][y+j] = num
                    elif cloth[x+i][y+j] != -1:
                        bad_nums.add(num)
                        bad_nums.add(cloth[x+i][y+j])
                        cloth[x+i][y+j] = -1
                        countoverlap += 1
                    else:
                        bad_nums.add(num)
if args.part == 1:                    
    print(countoverlap)
    
elif args.part == 2:
    print((total_nums ^ bad_nums).pop())
