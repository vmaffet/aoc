#!/usr/bin/python3

sketch = {}
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        sketch.update(
            {(x,y): c for x, c in enumerate(line.strip())}
        )

(sx,sy) = next(k for k,v in sketch.items() if v == 'S')

D = sketch[(sx,sy+1)] in {'|','L','J'}
U = sketch[(sx,sy-1)] in {'|','F','7'}
E = sketch[(sx+1,sy)] in {'-','J','7'}
W = sketch[(sx-1,sy)] in {'-','F','L'}
if U and D:
    sketch[(sx,sy)] = '|'
elif U and E:
    sketch[(sx,sy)] = 'L'
elif U and W:
    sketch[(sx,sy)] = 'J'
elif D and E:
    sketch[(sx,sy)] = 'F'
elif D and W:
    sketch[(sx,sy)] = '7'
elif E and W:
    sketch[(sx,sy)] = '-'

# ==== Part 1 ==== #
dist = {(sx,sy): 0}
queue = [(sx,sy)]
while queue:
    (x, y) = queue.pop(0)

    neighbors = []
    pipe = sketch[(x,y)]
    if pipe in {'|','L','J'}:
        neighbors.append((x, y-1))
    if pipe in {'|','F','7'}:
        neighbors.append((x, y+1))
    if pipe in {'-','J','7'}:
        neighbors.append((x-1, y))
    if pipe in {'-','F','L'}:
        neighbors.append((x+1, y))

    for p in neighbors:
        if p not in dist:
            dist[p] = dist[(x,y)] + 1
            queue.append(p)

print(max(dist.values()))

# ==== Part 2 ==== #
def countBoundXing(x, y):
    cnt, lastTurn = 0, ''
    for p in sorted([(a,b) for (a,b) in dist if a > x and b == y]):
        pipe = sketch[p]
        if pipe == '|':
            cnt += 1
        elif pipe in {'F','L'}:
            cnt += 1
            lastTurn = pipe
        elif pipe in {'7','J'}:
            if (pipe == '7' and lastTurn == 'F') or (pipe == 'J' and lastTurn == 'L'):
                cnt += 1
            lastTurn = ''
    return cnt

minX = min(p[0] for p in dist.keys())
maxX = max(p[0] for p in dist.keys())
minY = min(p[1] for p in dist.keys())
maxY = max(p[1] for p in dist.keys())

res = sum(
    countBoundXing(x, y) % 2 
    for x in range(minX, maxX+1) for y in range(minY, maxY+1)
    if (x,y) not in dist
)
print(res)
