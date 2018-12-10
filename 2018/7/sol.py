#!/usr/bin/python3
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

needs = defaultdict(lambda:set(), dict())
enables = defaultdict(lambda:set(), dict())

with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match(r'^Step (\w+) must be finished before step (\w+) can begin\.$', line)
        if matcher:
            up, down = matcher.groups()
            needs[down].add(up)
            enables[up].add(down)            

if args.part == 1:
    todo = enables.keys() - needs.keys()
    done = set()
    while todo:
        at = min(todo)
        todo.discard(at)
        done.add(at)
        for possbl in enables[at]:
            if done >= needs[possbl]:
                todo.add(possbl)
        print(at,end='')
    print('')
    
elif args.part == 2:
    workers = 5
    delay = 60
    
    todo = enables.keys() - needs.keys()
    working = dict()
    done = set()
    
    time = -1
    while todo or working:
        for key in list(working.keys()):
            if working[key] == 0:
                del working[key]
                done.add(key)
                for possbl in enables[key]:
                    if done >= needs[possbl]:
                        todo.add(possbl)
            else:
                working[key] -= 1
        
        while todo and len(working) < workers:
            at = min(todo)
            todo.discard(at)
            working[at] = delay + ord(at) - ord('A')
            
        time += 1
        
    print(time)
