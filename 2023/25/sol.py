#!/usr/bin/python3

from collections import Counter, defaultdict
import random

edges = defaultdict(set)
with open('input.txt', 'r') as f:
    for line in f:
        src, dsts = line.split(': ')
        for dst in dsts.split():
            edges[src].add(dst)
            edges[dst].add(src)

nodes = list(edges.keys())

# ==== Part 1 ==== #
def path(s, t):
    prev = {s:None}
    queue = [s]
    while queue:
        v = queue.pop(0)
        if v == t:
            break
        for n in edges[v]:
            if n not in prev:
                prev[n] = v
                queue.append(n)

    p = set()
    while v != s:
        n = prev[v]
        p.add(tuple(sorted((v, n))))
        v = n
    return p

c = Counter()
for _ in range(100):
    s, t = random.choice(nodes), random.choice(nodes)
    p = path(s, t)
    c.update(p)

# The 3 most common edges are likely to be the cut to seperate the two components
cut = {e for e,_ in c.most_common(3)}

explored = {nodes[0]}
queue = [nodes[0]]
while queue:
    v = queue.pop()
    for n in edges[v]:
        if n not in explored and tuple(sorted((v, n))) not in cut:
            explored.add(n)
            queue.append(n)

print(len(explored)*(len(nodes)-len(explored)))
