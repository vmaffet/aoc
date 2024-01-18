#!/usr/bin/python3

from itertools import pairwise

instructions = []
with open('input.txt', 'r') as f:
    for line in f:
        instructions.append(line.split())

direction = {'U':(0,-1), 'D':(0,1), 'L':(-1,0), 'R':(1,0)}

clockwiseOffset = {
    ('R','D'): (1, 0), ('D','L'): (1, 1),
    ('L','U'): (0, 1), ('U','R'): (0, 0),
    ('R','U'): (0, 0), ('U','L'): (0, 1),
    ('L','D'): (1, 1), ('D','R'): (1, 0)
}

def digmap(plan, clockwise):
    x = y = 0
    nodes = []
    for (d, n), (dNext,_) in pairwise(plan + plan[:1]):
        dx, dy = direction[d]
        x, y = x + n*dx, y + n*dy

        xOffset, yOffset = clockwiseOffset[(d,dNext)]
        if not clockwise:
            xOffset, yOffset = 1-xOffset, 1-yOffset
        nodes.append((x+xOffset,y+yOffset))
    return nodes

def lagoon(nodes):
    minY = min(y for _,y in nodes)
    area = 0
    for (xa,ya), (xb,_) in pairwise(nodes + nodes[:1]):
        a = (ya + minY + 1) * (xb - xa)
        area += a
    return int(abs(area))

# ==== Part 1 ==== #
digplan = [(d, int(n)) for d, n, _ in instructions]
print(max(lagoon(digmap(digplan, True)), lagoon(digmap(digplan, False))))

# ==== Part 2 ==== #
dec = ['R', 'D', 'L', 'U']
digplan = [(dec[int(c[-2])], int('0'+c[2:-2], 16)) for _, _, c in instructions]
print(max(lagoon(digmap(digplan, True)), lagoon(digmap(digplan, False))))
