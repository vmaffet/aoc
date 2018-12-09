#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

def reduce_pol(polymer):
    pos = 0
    while pos < len(polymer) - 1:
        sameletter = polymer[pos].lower() == polymer[pos+1].lower()
        samechar = ord(polymer[pos]) == ord(polymer[pos+1])
        if sameletter and not samechar:
            polymer = polymer[:pos] + polymer[pos+2:]
            pos = max(0, pos-1)
        else:
            pos += 1
    return polymer

with open(args.file, 'r') as f:
    data = f.read().strip()

if args.part == 1:
    
    out = reduce_pol(data)
    print(len(out))
   
elif args.part == 2:
    
    best_size = len(data)
    
    for i in range(26):
        c = chr(ord('a')+i)
        out = reduce_pol(data.replace(c, '').replace(c.upper(), ''))
        best_size = min(best_size, len(out))
        
    print(best_size)
