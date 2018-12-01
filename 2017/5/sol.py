#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    instructions = []    

    with open(args.file, 'r') as f:
        instructions = list(map(int, f.read().strip('\n').split('\n')))

    ite_count = 0
    pos = 0
    while pos >= 0 and pos < len(instructions):
        save = pos
        pos += instructions[save]
        instructions[save] += 1
        ite_count += 1

    print(ite_count)
    
elif args.part == 2:
    
    instructions = []    

    with open(args.file, 'r') as f:
        instructions = list(map(int, f.read().strip('\n').split('\n')))

    ite_count = 0
    pos = 0
    while pos >= 0 and pos < len(instructions):
        save = pos
        pos += instructions[save]
        instructions[save] += 1 if instructions[save] < 3 else -1
        ite_count += 1

    print(ite_count)
