#!/usr/bin/python3

garden = {}
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        garden.update(
            {(x,y): c for x, c in enumerate(line.strip())}
        )

width  = max(x for (x,_) in garden) + 1
height = max(y for (_,y) in garden) + 1
start = next(k for k,v in garden.items() if v == 'S')

def step(positions):
    newPositions = set()
    for x,y in positions:
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if garden[(nx%width, ny%height)] != '#':
                newPositions.add((nx,ny))
    return newPositions

def reach(n):
    pos = {start}
    for _ in range(n):
        pos = step(pos)
    return len(pos)

# ==== Part 1 ==== #
print(reach(64))

# ==== Part 2 ==== #
# Area grows according to a quadratic function for the specific puzzle input
N = 26501365
rem = N % 131
y0 = reach(rem + 131 * 0)
y1 = reach(rem + 131 * 1)
y2 = reach(rem + 131 * 2)

c = y0
a = ((y2 - c) - 2*(y1 - c)) // 2
b = y1 - a - c

x = N // 131
print(a*x*x + b*x + c)
