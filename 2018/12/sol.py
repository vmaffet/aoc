#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

pattern = dict()
        
with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match('([\.#]+) => ([\.#])', line)
        if matcher:
            pat, res = matcher.groups()
            pattern[pat] = res
        matcher = re.match('initial state: ([\.#]+)', line)
        if matcher:
            state = matcher.group(1)

def evolve(plants):
    plants = '.....' + plants + '.....'
    res = ''
    for i in range(len(plants)-5):
         res += pattern[plants[i:i+5]]
    return res
    
if args.part == 1:
    center = state.index('#')
    for i in range(20):
        state = evolve(state)
        center += 3 - state.index('#')
        state = state.strip('.')
    score = 0
    for i in range(len(state)):
        if state[i] == '#':
            score += i - center
    print(score)

elif args.part == 2:
    centerprev = 0
    center = state.index('#')
    prev = ''
    ite = 0
    while prev != state:
        ite += 1
        centerprev = center
        prev = state
        state = evolve(state)
        center += 3 - state.index('#')
        state = state.strip('.')
        
    center += (50000000000-ite)*(center-centerprev)
    
    score = 0
    for i in range(len(state)):
        if state[i] == '#':
            score += i - center
    print(score)
