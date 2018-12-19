#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

reg = [0]*4

op = [lambda a, b: reg[a] + reg[b],       # addr
      lambda a, b: reg[a] + b,            # addi
      lambda a, b: reg[a] * reg[b],       # mulr
      lambda a, b: reg[a] * b,            # muli
      lambda a, b: reg[a] & reg[b],       # banr
      lambda a, b: reg[a] & b,            # bani
      lambda a, b: reg[a] | reg[b],       # borr
      lambda a, b: reg[a] | b,            # bori
      lambda a, b: reg[a],                # setr
      lambda a, b: a,                     # seti
      lambda a, b: int(a > reg[b]),       # gtir
      lambda a, b: int(reg[a] > b),       # gtri
      lambda a, b: int(reg[a] > reg[b]),  # gtrr
      lambda a, b: int(a == reg[b]),      # eqir
      lambda a, b: int(reg[a] == b),      # eqri
      lambda a, b: int(reg[a] == reg[b])] # eqrr
      
      
def doop(opid, a, b, c):
    reg[c] = op[opid](a,b)
    
    
def setreg(a, b, c, d):
    global reg
    reg = [a, b, c, d]
    

def getreg():
    return reg


data = ''

with open(args.file, 'r') as f:
    data = f.read().strip()

samples, program = data.split('\n\n\n\n')

samples = [''.join(sample.split('\n')) for sample in samples.split('\n\n')]
program = program.split('\n')

if args.part == 1:
    count = 0
    for sample in samples:
        matcher = re.match(r'Before: \[([\d, ]+)\]([\d ]+)After:  \[([\d, ]+)\]', sample)
        if matcher:
            breg, inst, areg = matcher.groups()
            ba, bb, bc, bd = list(map(int, breg.split(', ')))
            io, ia, ib, ic = list(map(int, inst.split(' ')))
            areg = list(map(int, areg.split(', ')))
            valid = 0
            for i in range(len(op)):
                setreg(ba, bb, bc, bd)
                doop(i, ia, ib, ic)
                valid += 1 if areg == getreg() else 0
            count += 1 if valid >= 3 else 0
            
    print(count)

elif args.part == 2:
    mapping = {i:{j for j in range(len(op))} for i in range(len(op))}
    for sample in samples:
        matcher = re.match(r'Before: \[([\d, ]+)\]([\d ]+)After:  \[([\d, ]+)\]', sample)
        if matcher:
            breg, inst, areg = matcher.groups()
            ba, bb, bc, bd = list(map(int, breg.split(', ')))
            io, ia, ib, ic = list(map(int, inst.split(' ')))
            areg = list(map(int, areg.split(', ')))
            valid = 0
            for i in range(len(op)):
                setreg(ba, bb, bc, bd)
                doop(i, ia, ib, ic)
                if areg != getreg():
                    mapping[io].discard(i)
    
    while max(list(map(len, mapping.values()))) != 1:
        for key, value in mapping.items():
            if len(value) == 1:
                for okey in mapping.keys():
                    if okey != key:
                        mapping[okey] -= value
                
    mapping = {key:value.pop() for key, value in mapping.items()}
    
    setreg(0, 0, 0, 0)
    for line in program:
        o, a, b, c = list(map(int, line.split(' ')))
        doop(mapping[o], a, b, c)
        
    print(getreg()[0])
        
                    
