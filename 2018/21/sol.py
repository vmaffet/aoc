#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

reg = [0]*6

op = {'addr':lambda a, b: reg[a] + reg[b],
      'addi':lambda a, b: reg[a] + b,
      'mulr':lambda a, b: reg[a] * reg[b],
      'muli':lambda a, b: reg[a] * b,
      'banr':lambda a, b: reg[a] & reg[b],
      'bani':lambda a, b: reg[a] & b,
      'borr':lambda a, b: reg[a] | reg[b],
      'bori':lambda a, b: reg[a] | b,
      'setr':lambda a, b: reg[a],
      'seti':lambda a, b: a,
      'gtir':lambda a, b: int(a > reg[b]),
      'gtri':lambda a, b: int(reg[a] > b),
      'gtrr':lambda a, b: int(reg[a] > reg[b]),
      'eqir':lambda a, b: int(a == reg[b]),
      'eqri':lambda a, b: int(reg[a] == b),
      'eqrr':lambda a, b: int(reg[a] == reg[b])}
      
      
def doop(opid, a, b, c):
    reg[c] = op[opid](a,b)


insts = []

with open(args.file, 'r') as f:
    _, ip = f.readline().strip().split()
    ip = int(ip)
    for line in f:
        if line.strip():
            i, a, b, c = line.strip().split()
            a, b, c = int(a), int(b), int(c)
            insts.append((i, a, b, c))

if args.part == 1:
    while reg[ip] >= 0 and reg[ip] < len(insts):
        if reg[ip] == 28:
            print(reg[3])
            exit()
        i, a, b, c = insts[reg[ip]]
        doop(i, a, b, c)
        reg[ip] += 1
        print(reg)
    
elif args.part == 2:
    seen = set()
    c, d= 0, 0
    
    prev = 0
    while True:
        d = c | 65536
        c = 7041048
        
        while 256 <= d:
            c = (((c + (d & 255)) & 16777215 ) * 65899 ) & 16777215
            d = d // 256
            
        c = (((c + (d & 255)) & 16777215 ) * 65899 ) & 16777215
    
        if c in seen:
            print(prev)
            exit()
        else:
            seen.add(c)
            prev = c
            
            
        
        
        
