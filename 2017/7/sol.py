#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

checksum = 0
weights = dict()
above = dict()

with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match(r'^(\w+) \((\d+)\)(?: -> (.+))?$', line)
        if matcher:
            weights[matcher.group(1)] = int(matcher.group(2))
            if matcher.group(3):
                above[matcher.group(1)] = str(matcher.group(3)).split(', ')

notpossible = set()
for k in above.keys():
    for a in above[k]:
        if a in above:
            notpossible.add(a)

root = (above.keys() ^ notpossible).pop()
if args.part == 1:
    print(root)

if args.part == 2:
    
    change = dict()
    
    def balance(node):
        firstunbalanced = False
        res = 0
        if node in above:
            branches = [0]*len(above[node])
            for i in range(len(above[node])):
                branches[i], changed = balance(above[node][i])
                res += branches[i]
                if changed:
                    good, _ = balance(above[node][i-1])
                    if good > branches[i]:
                        for key in change:
                            if change[key] > weights[key]:
                                print('{} {} -> {}'.format(key, weights[key], change[key]))
                    else:
                        for key in change:
                            if change[key] <= weights[key]:
                                print('{} {} -> {}'.format(key, weights[key], change[key]))
                    exit()
            if max(branches) != min(branches):
                firstunbalanced = True
                for j in range(len(branches)):
                    if branches.count(branches[j]) == 1:
                        change[above[node][j]] = weights[above[node][j]] + branches[j-1]-branches[j]
            
        return (res + weights[node], firstunbalanced)
    
    balance(root)
        
