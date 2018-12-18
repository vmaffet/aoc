#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
        
with open(args.file, 'r') as f:
    n = int(f.read().strip())

scores = [3, 7]
length = 2

elf1 = 0
elf2 = 1
    
if args.part == 1:
    
    while length < n+10:
        x = scores[elf1] + scores[elf2]
        a, b = x // 10, x % 10
        if a != 0:
            scores.append(a)
            length += 1
        scores.append(b)
        length += 1
        elf1 = (elf1 + scores[elf1] + 1) % length
        elf2 = (elf2 + scores[elf2] + 1) % length
        
    print(''.join(map(str, scores[n:n+10])))

elif args.part == 2:
    
    token = str(n)
    
    while token not in ''.join(map(str, scores[-len(token)-1:])):
        x = scores[elf1] + scores[elf2]
        a, b = x // 10, x % 10
        if a != 0:
            scores.append(a)
            length += 1
        scores.append(b)
        length += 1
        elf1 = (elf1 + scores[elf1] + 1) % length
        elf2 = (elf2 + scores[elf2] + 1) % length
        
    print(''.join(map(str, scores)).index(token))

