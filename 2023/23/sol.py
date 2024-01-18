#!/usr/bin/python3

from collections import defaultdict

trails = {}
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        trails.update({(x,y): c for x, c in enumerate(line.strip())})

start = (1, 0)
end = (max(x for (x,_) in trails)-1, max(y for (_,y) in trails))

trails[(start[0], start[1]-1)] = '#'
trails[(end[0], end[1]+1)] = '#'

def outward(x,y):
    return {
        (x+dx,y+dy)
        for dx,dy,uphill in [(1,0,'<'),(-1,0,'>'),(0,1,'^'),(0,-1,'v')]
        if trails[(x+dx,y+dy)] not in {uphill,'#'}
    }

def junction(x,y):
    return (x,y) == end or sum(
        trails[(x+dx,y+dy)] in '<^>v'
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]
    ) > 1

edges = defaultdict(list)

queue = [(p,start,1) for p in outward(*start)]
visited = {start}
while queue:
    (cur,prev,n) = queue.pop()
    if junction(*cur) and prev != cur:
        edges[prev].append((cur, n))

    if cur not in visited:
        visited.add(cur)
        for p in outward(*cur):
            queue.append((p, cur, 1) if junction(*cur) else (p, prev, n+1))

# ==== Part 1 ==== #
dist = {start:0}
queue = [start]
while queue:
    cur = queue.pop(0)
    for (B,N) in edges[cur]:
        queue.append(B)
        dist[B] = max(dist.get(B,0), dist[cur] + N)

print(dist[end])

# ==== Part 2 ==== #
edges2 = defaultdict(list)
for A in edges:
    for (B,N) in edges[A]:
        edges2[A].append((B,N))
        edges2[B].append((A,N))

def longest(pos, visited, n):
    if pos == end:
        return n

    visited.add(pos)
    return max((longest(B, visited.copy(), n + N) for (B,N) in edges2[pos] if B not in visited), default=0)

print(longest(start, set(), 0))
