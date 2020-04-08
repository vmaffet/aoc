#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

infected = set()
with open(args.file, 'r') as f:
    for j,line in enumerate(f):
        infected.update([(i,j) for i,e in enumerate(line) if e == '#'])

carrier = (i//2, j//2, 'NORTH')

if args.part == 1:
    moves = {'EAST': lambda x,y,t: (x,   y+t, 'SOUTH' if t>0 else 'NORTH'),
             'NORTH':lambda x,y,t: (x+t, y,   'EAST'  if t>0 else 'WEST'),
             'WEST': lambda x,y,t: (x,   y-t, 'NORTH' if t>0 else 'SOUTH'),
             'SOUTH':lambda x,y,t: (x-t, y,   'WEST'  if t>0 else 'EAST')}

    bursts = 10000
    infections = 0
    for i in range(bursts):
        x, y, o = carrier
        
        t = 1 if (x,y) in infected else -1
        
        if (x,y) in infected:
            infected.discard((x,y))
        else:
            infected.add((x,y))
            infections += 1
        
        carrier = moves[o](x,y,t)

    print(infections)

elif args.part == 2:
    weakened = set()
    flagged = set()
    
    moves = {('EAST','RIGHT'):    lambda x,y: (x,y+1,'SOUTH'),
             ('EAST','REVERSE'):  lambda x,y: (x-1,y,'WEST'),
             ('EAST','STRAIGHT'): lambda x,y: (x+1,y,'EAST'),
             ('EAST','LEFT'):     lambda x,y: (x,y-1,'NORTH'),
             ('NORTH','RIGHT'):   lambda x,y: (x+1,y,'EAST'),
             ('NORTH','REVERSE'): lambda x,y: (x,y+1,'SOUTH'),
             ('NORTH','STRAIGHT'):lambda x,y: (x,y-1,'NORTH'),
             ('NORTH','LEFT'):    lambda x,y: (x-1,y,'WEST'),
             ('WEST','RIGHT'):    lambda x,y: (x,y-1,'NORTH'),
             ('WEST','REVERSE'):  lambda x,y: (x+1,y,'EAST'),
             ('WEST','STRAIGHT'): lambda x,y: (x-1,y,'WEST'),
             ('WEST','LEFT'):     lambda x,y: (x,y+1,'SOUTH'),
             ('SOUTH','RIGHT'):   lambda x,y: (x-1,y,'WEST'),
             ('SOUTH','REVERSE'): lambda x,y: (x,y-1,'NORTH'),
             ('SOUTH','STRAIGHT'):lambda x,y: (x,y+1,'SOUTH'),
             ('SOUTH','LEFT'):    lambda x,y: (x+1,y,'EAST')}

    bursts = 10000000
    infections = 0
    for i in range(bursts):
        x, y, o = carrier
        
        if (x,y) in infected:
            t = 'RIGHT'
            infected.discard((x,y))
            flagged.add((x,y))
            
        elif (x,y) in flagged:
            t = 'REVERSE'
            flagged.discard((x,y))
        
        elif (x,y) in weakened:
            t = 'STRAIGHT'
            weakened.discard((x,y))
            infected.add((x,y))
            infections += 1
        
        else:
            t = 'LEFT'
            weakened.add((x,y))
        
        carrier = moves[(o,t)](x,y)

    print(infections)