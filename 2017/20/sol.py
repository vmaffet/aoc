#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    best_particule = -1
    min_p = float('inf')
    min_v = float('inf')
    min_a = float('inf')
    
    pid = 0
    with open(args.file, 'r') as f:
        for line in f:
            matcher = re.match(r'^p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>$', line)
            if matcher:
                px, py, pz, vx, vy, vz, ax, ay, az = list(map(int, matcher.groups()))
                nm_p = abs(px) + abs(py) + abs(pz)
                nm_v = abs(vx) + abs(vy) + abs(vz)
                nm_a = abs(ax) + abs(ay) + abs(az)
                if nm_a < min_a or (nm_a == min_a and nm_v < min_v) or (nm_a == min_a and nm_v == min_v and nm_p < min_p):
                    min_p = nm_p
                    min_v = nm_v
                    min_a = nm_a
                    best_particule = pid
                
            pid += 1
        
    print(best_particule)
    
if args.part == 2:
    
    # Dirty simulation with no clean end condition
    
    particules = []
    
    with open(args.file, 'r') as f:
        for line in f:
            matcher = re.match(r'^p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>$', line)
            if matcher:
                particules.append(list(map(int, matcher.groups())))
    
    def posAtTime(pid, t):
        px, py, pz, vx, vy, vz, ax, ay, az = particules[pid]
        return (px+t*vx+(t+1)*t*ax/2, py+t*vy+(t+1)*t*ay/2, pz+t*vz+(t+1)*t*az/2)
    
    n = 1000
    
    alive = set([i for i in range(len(particules))])
    for i in range(n):
        positions = {}
        dead = set()
        for pid in alive:
            pos = posAtTime(pid, i)
            for (pi,po) in positions.items():
                if pos == po:
                    dead.add(pi)
                    dead.add(pid)
                    continue
            positions[pid] = posAtTime(pid, i)
        alive -= dead
    
    print(len(alive))
            
        
    
