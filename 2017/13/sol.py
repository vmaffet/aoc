#!/usr/bin/python3
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    severity = 0

    with open(args.file, 'r') as f:
        for line in f:
            matcher = re.match(r'^(\d+): (\d+)', line)
            if matcher:
                loc = int(matcher.group(1))
                depth = int(matcher.group(2))
                if loc % (2*depth-2) == 0:
                    severity += loc*depth

    print(severity)

if args.part == 2:
    
    firewall = []
    with open(args.file, 'r') as f:
        for line in f:
            matcher = re.match(r'^(\d+): (\d+)', line)
            if matcher:
                loc = int(matcher.group(1))
                depth = int(matcher.group(2))
                firewall.append((loc, depth))
                
    delay = 0
    caught = True
    while caught:
        caught = False
        for (l,d) in firewall:
            if (l+delay) % (2*d-2) == 0:
                delay += 1
                caught = True
                break
    
    print(delay)
