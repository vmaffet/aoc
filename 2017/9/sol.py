#!/usr/bin/python3
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()


data = ''

with open(args.file, 'r') as f:
    data = f.read().strip('\n')


score = 0
value = 1
garbage_count = 0
garbage = False
ignore_next = False
for c in data:
    if ignore_next:
        ignore_next = False
    elif garbage:
        if c == '!':
            ignore_next = True
        elif c == '>':
            garbage = False
        else:
            garbage_count += 1
    else:
        if c == '!':
            ignore_next = True
        elif c == '<':
            garbage = True
        elif c == '{':
            score += value
            value += 1
        elif c == '}':
            value -= 1
            
if args.part == 1:
    print(score)

if args.part == 2:
    print(garbage_count)
