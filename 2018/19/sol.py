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
        i, a, b, c = insts[reg[ip]]
        doop(i, a, b, c)
        reg[ip] += 1
    print(reg[0])
    
elif args.part == 2: # analysed the assembly
    n = (2**2)*19*11 + 6*22 + 2 + (27*28 + 29 )*30*14*32
    print(sum([c if (n % c) == 0 else 0 for c in range(1,n+1)]))
  
