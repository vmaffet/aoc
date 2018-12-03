#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
   
moves = []
with open(args.file, 'r') as f:
    moves = f.read().strip('\n').split(',')

def doDance(positions):
    
    for mv in moves:
        matcher = re.match(r's(\d+)', mv)
        if matcher:
            spin = int(matcher.group(1))
            positions = positions[-spin:] + positions[:-spin]
        matcher = re.match(r'x(\d+)/(\d+)', mv)
        if matcher:
            x1 = int(matcher.group(1))
            x2 = int(matcher.group(2))
            if x1 > x2:
                x1, x2 = x2, x1
            positions = positions[:x1] + [positions[x2]] + positions[x1+1:x2] + [positions[x1]] + positions[x2+1:]
        matcher = re.match(r'p(\w+)/(\w+)', mv) 
        if matcher:
            x1 = positions.index(ord(matcher.group(1))-ord('a'))
            x2 = positions.index(ord(matcher.group(2))-ord('a'))
            if x1 > x2:
                x1, x2 = x2, x1
            positions = positions[:x1] + [positions[x2]] + positions[x1+1:x2] + [positions[x1]] + positions[x2+1:] 
    
    return positions

if args.part == 1:
    
    dance = doDance([ i for i in range(16) ])     
    print(''.join([ chr(ord('a')+i) for i in dance]))
    
if args.part == 2:
    
    dance = [ [ i for i in range(16) ] ]
    dance.append(doDance(dance[-1]))    
    while dance[-1] != dance[0]:
        dance.append(doDance(dance[-1]))
    dance.pop()
    
    print(''.join([ chr(ord('a')+i) for i in dance[1000000000 % len(dance)]]))
