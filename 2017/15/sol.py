#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
   
A = B = 0
with open(args.file, 'r') as f:
    matcher = re.match(r'.*?(\d+)\n.*?(\d+)', f.read())
    if matcher:
        A = int(matcher.group(1))
        B = int(matcher.group(2))

fA = 16807
fB = 48271

n = 2147483647
    
if args.part == 1:        
        
    count = 0
    for i in range(40000000):
        A = (fA * A) % n
        B = (fB * B) % n
        if bin(A)[-16:] == bin(B)[-16:]:
            count += 1
    
    print(count)

if args.part == 2:
    
    count = 0
    for i in range(5000000):
        A = (fA * A) % n
        B = (fB * B) % n
        while A % 4 != 0:
            A = (fA * A) % n
        while B % 8 != 0:
            B = (fB * B) % n
        if bin(A)[-16:] == bin(B)[-16:]:
            count += 1
    
    print(count)
