#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
    
past = dict()    

banks = []
with open(args.file, 'r') as f:
    banks = list(map(int, f.read().strip('\n').split('\t')))

n = len(banks)    

ite_count = 0
while tuple(banks) not in past:
    past[tuple(banks)] = ite_count
    
    treat = banks.index(max(banks))        
    distribute = banks[treat]
    banks[treat] = 0
    for i in range(n):
        banks[(treat+i+1)%n] += distribute//n + (1 if i < distribute % n else 0)
    ite_count += 1

print('ite: {}\nlenght: {}'.format(ite_count, ite_count-past[tuple(banks)]))
