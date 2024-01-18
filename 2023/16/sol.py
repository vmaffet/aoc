#!/usr/bin/python3

layout = {}
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        layout.update(
            {(x,y): c for x, c in enumerate(line.strip())}
        )

width  = max(x for (x,_) in layout) + 1
height = max(y for (_,y) in layout) + 1

NORTH, SOUTH, EAST, WEST = (0,-1), (0,1), (1,0), (-1,0)
mirrors = {
    '|':  {NORTH: [NORTH],     SOUTH: [SOUTH],     EAST: [NORTH,SOUTH], WEST: [NORTH,SOUTH]},
    '-':  {NORTH: [EAST,WEST], SOUTH: [EAST,WEST], EAST: [EAST],        WEST: [WEST]},
    '/':  {NORTH: [EAST],      SOUTH: [WEST],      EAST: [NORTH],       WEST: [SOUTH]},
    '\\': {NORTH: [WEST],      SOUTH: [EAST],      EAST: [SOUTH],       WEST: [NORTH]},
    '.':  {NORTH: [NORTH],     SOUTH: [SOUTH],     EAST: [EAST],        WEST: [WEST]},
}

def energized(start):
    visited = {}
    queue = [start]
    while queue:
        (x, y, d) = queue.pop()

        nx, ny = x+d[0], y+d[1]
        if (nx, ny) not in layout:
            continue

        for nd in mirrors[layout[(nx, ny)]][d]:
            if (nx, ny, nd) not in visited:
                visited[(nx, ny, nd)] = True
                queue.append((nx, ny, nd))

    return len({(x,y) for (x,y,_) in visited})

# ==== Part 1 ==== #
print(energized((-1, 0, EAST)))

# ==== Part 2 ==== #
maxWest  = max(energized((-1,    y,      EAST))  for y in range(height))
maxEast  = max(energized((width, y,      WEST))  for y in range(height))
maxNorth = max(energized((x,    -1,      SOUTH)) for x in range(width))
maxSouth = max(energized((x,     height, NORTH)) for x in range(width))
print(max([maxWest, maxEast, maxSouth, maxNorth]))
