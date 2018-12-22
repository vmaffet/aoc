#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
    
routes = ''    

with open(args.file, 'r') as f:
    routes = f.read().strip()
    
    
def parsep(line):
    lpar, rpar = None, None
    countLpar = 0
    for i in range(len(line)):
        if line[i] == '(':
            if countLpar == 0:
                lpar = i
            countLpar += 1
        elif line[i] == ')':
            countLpar -= 1
            if countLpar == 0:
                rpar = i
                return line[:lpar], line[lpar+1:rpar], line[rpar+1:]
    return line, '', ''

def pipesep(line):
    start = 0
    parts = []
    countLpar = 0
    for i in range(len(line)):
        if line[i] == '|':
          if countLpar == 0:
              parts.append(line[start:i])
              start = i+1  
        elif line[i] == '(':
            countLpar += 1
        elif line[i] == ')':
            countLpar -= 1
    parts.append(line[start:len(line)])
    return parts
    

limit = 999
count1000 = 0
def lengths(line, n):
    global count1000
    records = []        
    parts = pipesep(line)
    if '' in parts:
        for p in parts:
            if n + len(p)/2 > limit:
                count1000 += int(len(p)/2) - ((limit - n) if n < limit else 0) # not exactly working... should build the graph and run bfs to be sure, the input path is not optimized
        return [0]
    for p in parts:
        fl, ml, bl = parsep(p)
        l = len(fl)
        if n + l > limit:
            count1000 += l - ((limit - n) if n < limit else 0)
        mls = lengths(ml, n+l)
        for m in mls:
            bls = lengths(bl, n+l+m)
            for b in bls:
                records.append(l+m+b)
    return records
    

res = lengths(routes[1:-1], 0)    

if args.part == 1:
    print(max(res))

elif args.part == 2:
    print(count1000)
        
