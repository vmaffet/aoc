#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
   
with open(args.file, 'r') as f:
    steps = int(f.read().strip('\n'))

if args.part == 1:
    
    pos = 0
    mem = [0]
    for i in range(2017):
        pos = ((pos + steps) % (i+1)) + 1
        mem = mem[:pos] + [i+1] + mem[pos:]
        
    print(mem[mem.index(2017)+1])
    
if args.part == 2:
    
    pos = 0
    current = 0
    for i in range(50000000):
        pos = ((pos + steps) % (i+1)) + 1
        if pos == 1:
            current = i+1
        
    print(current)
