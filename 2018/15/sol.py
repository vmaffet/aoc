#!/usr/bin/python3
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
parser.add_argument("-d", "--disp", help="disp", type=bool, default=False)
args = parser.parse_args()

terrain = []

def loadgame():
    terrain.clear()
    with open(args.file, 'r') as f:
        for line in f:
            if line.strip():
                terrain.append(list(line.strip()))

    pid = 0
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            if terrain[y][x] in 'GE':
                terrain[y][x] = (terrain[y][x], pid, 200)
                pid += 1 
            else:
                terrain[y][x] = (terrain[y][x])


def dispTerrain():
    print('\n'.join([(''.join([item[0] for item in row]) + ''.join(['({})'.format(item[2]) if len(item) > 1 else '' for item in row])) for row in terrain]))
    
      
def move(x, y):
    faction, pid, hp = terrain[y][x]
    trail = dict()
    done = {(x, y)}
    totry = [(x, y, 0)]
    goal = None
    while totry:
        tx, ty, d = totry.pop(0)
        trail[(tx, ty)] = d
        if terrain[ty][tx][0] not in '#.'+faction:
            goal = (tx, ty)
            break
        if terrain[ty-1][tx][0] not in '#'+faction and (tx, ty-1) not in done:
            totry.append((tx, ty-1, d+1))
            done.add((tx, ty-1))
        if terrain[ty][tx-1][0] not in '#'+faction and (tx-1, ty) not in done:
            totry.append((tx-1, ty, d+1))
            done.add((tx-1, ty))
        if terrain[ty][tx+1][0] not in '#'+faction and (tx+1, ty) not in done:
            totry.append((tx+1, ty, d+1))
            done.add((tx+1, ty))
        if terrain[ty+1][tx][0] not in '#'+faction and (tx, ty+1) not in done:
            totry.append((tx, ty+1, d+1))
            done.add((tx, ty+1))
    
    if goal is None or trail[goal] == 1:
        return x, y
    else:
        gx, gy = goal
        while trail[(gx, gy)] > 1:
            newgoal = None
            if (gx, gy-1) in trail and (newgoal is None or trail[(gx, gy-1)] < trail[newgoal]):
                newgoal = (gx, gy-1)
            if (gx-1, gy) in trail and (newgoal is None or trail[(gx-1, gy)] < trail[newgoal]):
                newgoal = (gx-1, gy)
            if (gx+1, gy) in trail and (newgoal is None or trail[(gx+1, gy)] < trail[newgoal]):
                newgoal = (gx+1, gy)
            if (gx, gy+1) in trail and (newgoal is None or trail[(gx, gy+1)] < trail[newgoal]):
                newgoal = (gx, gy+1)
            gx, gy = newgoal
        
        terrain[gy][gx], terrain[y][x] = terrain[y][x], ('.')
        return gx, gy
        
    
def attack(x, y, power):
    ax, ay = None, None
    if terrain[y-1][x][0] not in '#.'+terrain[y][x][0]:
        if (ax is None and ay is None) or terrain[y-1][x][2] < terrain[ay][ax][2]:
            ax, ay = x, y-1
    if terrain[y][x-1][0] not in '#.'+terrain[y][x][0]:
        if (ax is None and ay is None) or terrain[y][x-1][2] < terrain[ay][ax][2]:
            ax, ay = x-1, y
    if terrain[y][x+1][0] not in '#.'+terrain[y][x][0]:
        if (ax is None and ay is None) or terrain[y][x+1][2] < terrain[ay][ax][2]:
            ax, ay = x+1, y
    if terrain[y+1][x][0] not in '#.'+terrain[y][x][0]:
        if (ax is None and ay is None) or terrain[y+1][x][2] < terrain[ay][ax][2]:
            ax, ay = x, y+1
    if ax is not None and ay is not None:
        if terrain[ay][ax][2] > power:
            terrain[ay][ax] = (terrain[ay][ax][0], terrain[ay][ax][1], terrain[ay][ax][2]-power)
        else:
            terrain[ay][ax] = ('.')
            

def doturn(x, y, elfpower):
    x, y = move(x, y)
    attack(x, y, 3 if terrain[y][x][0] == 'G' else elfpower)

      
def doround(elfpower):
    played = set()
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            if terrain[y][x][0] in 'GE':
                faction, pid, hp = terrain[y][x]
                if pid not in played:
                    if twoteams():
                        doturn(x, y, elfpower)
                        played.add(pid)
                    else:
                        return False
    return True
    
def twoteams():
    foundG = False
    foundE = False
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            if terrain[y][x][0] == 'E':
                foundE = True
            if terrain[y][x][0] == 'G':
                foundG = True
        if foundE and foundG:
            return True
    return False
    
    
def score():
    score = 0
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            if terrain[y][x][0] not in '#.':
                score += terrain[y][x][2]
    return score
    

def numberofelfs():
    elfcount = 0
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            if terrain[y][x][0] == 'E':
                elfcount += 1
    return elfcount
    
    
if args.part == 1:
    loadgame()
    roundNumber = 0
    while twoteams():
        full = doround(3)
        if full:
            roundNumber += 1
        if args.disp:
            print(roundNumber)
            dispTerrain()
            time.sleep(0.1)
    
    print(roundNumber*score())
    
elif args.part == 2:
    elfpower = 0
    elfdied = True
    while elfdied:
        elfpower += 1
        loadgame()
        nelfs = numberofelfs()
        roundNumber = 0
        while twoteams() and numberofelfs() == nelfs:
            full = doround(elfpower)
            if full:
                roundNumber += 1
            if args.disp:
                print(roundNumber, elfpower)
                dispTerrain()
                time.sleep(0.01)
                
        elfdied = numberofelfs() < nelfs
    
    print(roundNumber*score())

