#!/usr/bin/python3
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
   
instrctns = []
with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match(r'(\w+) (-?\w+)(?: (-?\w+))?$', line)
        if matcher:
            instrctns.append(matcher.groups())

if args.part == 1:
    
    regstrs = defaultdict(lambda:0, dict())
    
    nxt = 0
    playing = 0
    
    while nxt >= 0 and nxt < len(instrctns):
        (name, x, y) = instrctns[nxt]
        if name == 'snd':
            if re.match(r'-?\d+', x):
                playing = int(x)
            else:
                playing = regstrs[x]
        elif name == 'set':
            if re.match(r'-?\d+', y):
                regstrs[x] = int(y)
            else:
                regstrs[x] = regstrs[y]
        elif name == 'add':
            if re.match(r'-?\d+', y):
                regstrs[x] += int(y)
            else:
                regstrs[x] += regstrs[y]
        elif name == 'mul':
            if re.match(r'-?\d+', y):
                regstrs[x] *= int(y)
            else:
                regstrs[x] *= regstrs[y]
        elif name == 'mod':
            if re.match(r'-?\d+', y):
                regstrs[x] %= int(y)
            else:
                regstrs[x] %= regstrs[y]
        elif name == 'rcv':
            if re.match(r'-?\d+', x):
                r = int(x)
            else:
                r = regstrs[x]
            if r != 0:
                break
        elif name == 'jgz':
            if regstrs[x] > 0:
                if re.match(r'-?\d+', y):
                    nxt += int(y)
                else:
                    nxt += regstrs[y]
                continue
        nxt += 1
    
    print(playing)
    
if args.part == 2:
    
    regstrs = [defaultdict(lambda:0, dict()), defaultdict(lambda:0, dict())]
    regstrs[0]['p'] = 0
    regstrs[1]['p'] = 1
    
    nxt = [0, 0]
    queue = [[], []]
    
    count1send = 0
    
    def do_iter(pid):
        global count1send
        if nxt[pid] < 0 or nxt[pid] >= len(instrctns):
            return False
        (name, x, y) = instrctns[nxt[pid]]
        if name == 'snd':
            count1send += 1 if pid == 1 else 0
            if re.match(r'-?\d+', x):
                queue[(pid+1)%2].append(int(x))
            else:
                queue[(pid+1)%2].append(regstrs[pid][x])
        elif name == 'set':
            if re.match(r'-?\d+', y):
                regstrs[pid][x] = int(y)
            else:
                regstrs[pid][x] = regstrs[pid][y]
        elif name == 'add':
            if re.match(r'-?\d+', y):
                regstrs[pid][x] += int(y)
            else:
                regstrs[pid][x] += regstrs[pid][y]
        elif name == 'mul':
            if re.match(r'-?\d+', y):
                regstrs[pid][x] *= int(y)
            else:
                regstrs[pid][x] *= regstrs[pid][y]
        elif name == 'mod':
            if re.match(r'-?\d+', y):
                regstrs[pid][x] %= int(y)
            else:
                regstrs[pid][x] %= regstrs[pid][y]
        elif name == 'rcv':
            if queue[pid]:
                regstrs[pid][x] = queue[pid].pop(0)
            else:
                return False
        elif name == 'jgz':
            if re.match(r'-?\d+', x):
                j = int(x)
            else:
                j = regstrs[pid][x]
            if j > 0:
                if re.match(r'-?\d+', y):
                    nxt[pid] += int(y)
                else:
                    nxt[pid] += regstrs[pid][y]
                return True
        nxt[pid] += 1
        return True
    
    ok0 = ok1 = True
    while ok0 or ok1:
        ok0 = do_iter(0)
        ok1 = do_iter(1)
        
    print(count1send)
