#!/usr/bin/python3
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

rules = {}

def np_2_str(arr):
    return '/'.join([''.join(['#' if e else '.' for e in row]) for row in arr])

with open(args.file, 'r') as f:
    for line in f:
        a, b = line.strip().split(' => ')
        
        npa = np.array([[c == '#' for c in row] for row in a.split('/')])
        npb = np.array([[c == '#' for c in row] for row in b.split('/')])
        
        rules[np_2_str(npa)] = npb
        rules[np_2_str(npa[::-1])] = npb
        rules[np_2_str(npa[:,::-1])] = npb
        rules[np_2_str(npa[::-1,::-1])] = npb
        rules[np_2_str(npa.T)] = npb
        rules[np_2_str(npa[::-1].T)] = npb
        rules[np_2_str(npa[:,::-1].T)] = npb
        rules[np_2_str(npa[::-1,::-1].T)] = npb

grid = np.array([[c == '#' for c in row] for row in '.#./..#/###'.split('/')])

if args.part == 1:
    ite = 5

elif args.part == 2:
    ite = 18

for i in range(ite):
    
    size, _ = grid.shape
    if size % 2 == 0:
        new_size = 3*size//2
        new_grid = np.zeros((new_size,new_size),dtype=bool)
        
        for x in range(size//2):
            for y in range(size//2):
                part = grid[2*y:2*y+2,2*x:2*x+2]
                new_grid[3*y:3*y+3,3*x:3*x+3] = rules[np_2_str(part)]
    
    elif size % 3 == 0:
        new_size = 4*size//3
        new_grid = np.zeros((new_size,new_size),dtype=bool)
        
        for x in range(size//3):
            for y in range(size//3):
                part = grid[3*y:3*y+3,3*x:3*x+3]
                new_grid[4*y:4*y+4,4*x:4*x+4] = rules[np_2_str(part)]
    
    grid = new_grid

print(grid.sum())
