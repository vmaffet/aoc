#!/usr/bin/python3
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

graph = defaultdict(lambda:[], dict())

with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match(r'^(\d+) <-> ([\d, ]+)', line)
        if matcher:
            num = int(matcher.group(1))
            neighbors = list(map(int, matcher.group(2).split(', ')))
            graph[num] = neighbors

scc = dict()
current_scc = 0

for k in graph.keys():
    if k not in scc:
        current = k
        scc[current] = current_scc
        tovisit = graph[current]
        while tovisit:
            current = tovisit.pop()
            if current not in scc:
                scc[current] = current_scc
                tovisit.extend(graph[current])
        current_scc += 1
            
if args.part == 1:
    print(len([k for k,v in scc.items() if v == scc[0]]))

if args.part == 2:
    print(current_scc)
