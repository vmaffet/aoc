#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()
   
diagram = []
with open(args.file, 'r') as f:
    for line in f:
        if line.strip('\n'):
            diagram.append(list(line.strip('\n')))

tracking = ''
count = 0

y = 0
x = diagram[y].index('|')
heading = 'S'
while diagram[y][x] != ' ':
    count += 1
    if diagram[y][x] == '+':
        
        if heading == 'E':
            if diagram[y+1][x] != ' ':
                y += 1
                heading = 'S'
            else:
                y -= 1
                heading = 'N'
        elif heading == 'N':
            if diagram[y][x+1] != ' ':
                x += 1
                heading = 'E'
            else:
                x -= 1
                heading = 'W'
        elif heading == 'W':
            if diagram[y-1][x] != ' ':
                y -= 1
                heading = 'N'
            else:
                y += 1
                heading = 'S'
        elif heading == 'S':
            if diagram[y][x-1] != ' ':
                x -= 1
                heading = 'W'
            else:
                x += 1
                heading = 'E'
        continue
        
    elif diagram[y][x].isalpha():
         tracking += diagram[y][x]
    
    if heading == 'E':
        x += 1
    elif heading == 'N':
        y -= 1
    elif heading == 'W':
        x -= 1
    elif heading == 'S':
        y += 1


if args.part == 1:
    print(tracking)
    
if args.part == 2:
    print(count)
