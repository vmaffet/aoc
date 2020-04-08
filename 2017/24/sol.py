#!/usr/bin/python3
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

connectors = dict()
by_type = defaultdict(set)
count = 0
with open(args.file, 'r') as f:
    for line in f:
        a, b = map(int,line.strip().split('/'))
        connectors[count] = (a,b,1,a+b)
        by_type[a].add(count)
        by_type[b].add(count)
        count += 1

for end_type in by_type:
    if end_type != 0 and len(by_type[end_type]) == 2:
        a, b = by_type[end_type]
        
        (ax, ay, al, ap) = connectors[a]
        (bx, by, bl, bp) = connectors[b]
        
        x = ay if end_type == ax else ax
        y = by if end_type == bx else bx
        
        connectors[count] = (x, y, al+bl, ap+bp)
        by_type[end_type].clear()
        by_type[x].discard(a)
        by_type[y].discard(b)
        by_type[x].add(count)
        by_type[y].add(count)
        del connectors[a]
        del connectors[b]
        
        count += 1
    
    elif len(by_type[end_type]) == 3:
        a, b, c = by_type[end_type]
        
        (ax, ay, al, ap) = connectors[a]
        (bx, by, bl, bp) = connectors[b]
        (cx, cy, cl, cp) = connectors[c]
        
        if ax == ay:
            x = by if end_type == bx else bx
            y = cy if end_type == cx else cx
            by_type[x].discard(b)
            by_type[y].discard(c)
        elif bx == by:
            x = ay if end_type == ax else ax
            y = cy if end_type == cx else cx
            by_type[x].discard(a)
            by_type[y].discard(c)
        elif cx == cy:
            x = ay if end_type == ax else ax
            y = by if end_type == bx else bx
            by_type[x].discard(a)
            by_type[y].discard(b)
        else:
            continue
            
        connectors[count] = (x, y, al+bl+cl, ap+bp+cp)
        by_type[end_type].clear()
        by_type[x].add(count)
        by_type[y].add(count)
        del connectors[a]
        del connectors[b]
        del connectors[c]
        
        count += 1

by_type = {k:v for k,v in by_type.items() if v}

if args.part == 1:
    def elongate(end, used):
        tried = set()
        best = 0
        for part in sorted(by_type[end], key=lambda x:connectors[x][-1], reverse=True):
            if part not in used:
                x, y, l, s = connectors[part]
                if (x,y) not in tried:
                    tried.add((x,y))
                    new_end = y if x == end else x
                    score = elongate(new_end, used.union({part}))
                    best = max(best, score+s)
                    
        return best    

    bridge = set()
    last = 0
    best = elongate(last, bridge)
    print(best)
        
elif args.part == 2:
    def elongate(end, used):
        tried = set()
        best = (0,0)
        for part in sorted(by_type[end], key=lambda x:connectors[x][2:], reverse=True):
            if part not in used:
                x, y, l, s = connectors[part]
                if (x,y) not in tried:
                    tried.add((x,y))
                    new_end = y if x == end else x
                    (length, score) = elongate(new_end, used.union({part}))
                    best = max(best, (length+l,score+s))
                    
        return best    

    bridge = set()
    last = 0
    (length, score) = elongate(last, bridge)
    print(length, score)