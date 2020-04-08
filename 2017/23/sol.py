#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

program = []
with open(args.file, 'r') as f:
    for line in f:
        program.append(line.strip().split())

if args.part == 1:
    mul_count = 0

    reg = {r:0 for r in 'abcdefgh'}
    inst_pointer = 0

    while inst_pointer < len(program):
        inst, op_1, op_2 = program[inst_pointer]
        
        if inst == 'set':
            if op_2 in reg:
                reg[op_1] = reg[op_2]
            else:    
                reg[op_1] = int(op_2)
                
        elif inst == 'sub':
            if op_2 in reg:
                reg[op_1] -= reg[op_2]
            else:    
                reg[op_1] -= int(op_2)
                
        elif inst == 'mul':
            mul_count += 1
            if op_2 in reg:
                reg[op_1] *= reg[op_2]
            else:    
                reg[op_1] *= int(op_2)
                
        elif inst == 'jnz':
            if (op_1 in reg and reg[op_1]) or (op_1 not in reg and int(op_1)):    
                inst_pointer += int(op_2)-1
        
        inst_pointer += 1
    
    print(mul_count)
        
elif args.part == 2:
    B0 = 108400
    C = 125400
    H = 0

    for B in range(B0,C+1,17):

        F = 1
        
        for X in range(2,int(B**0.5)):
            if B % X == 0:
                F = 0
                break
                
        if F == 0:
            H += 1

    print(H)