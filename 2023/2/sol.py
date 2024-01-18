#!/usr/bin/python3

import re

games = []
with open('input.txt', 'r') as f:
    for line in f:
        games += re.findall(r'Game \d+: (.+)', line)

# ==== Part 1 ==== #
limit = {'red': 12, 'green': 13, 'blue': 14}

res = 0
for i, g in enumerate(games):
    ok = True
    for cube in re.split(r'[,;]', g):
        n, color = cube.strip().split()
        if limit[color] < int(n):
            ok = False
            break
    if ok:
        res += i + 1
print(res)

# ==== Part 2 ==== #
res = 0
for i, g in enumerate(games):
    maxv = {'red': 0, 'green': 0, 'blue': 0}
    for cube in re.split(r'[,;]', g):
        n, color = cube.strip().split()
        maxv[color] = max(maxv[color], int(n))
    res += maxv['red'] * maxv['green'] * maxv['blue']
print(res)
