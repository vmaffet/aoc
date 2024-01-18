#!/usr/bin/python3

from collections import defaultdict
import re

schema = []
with open('input.txt', 'r') as f:
    for line in f:
        schema.append('.' + line.strip() + '.')
schema = ['.'*len(schema[0])] + schema + ['.'*len(schema[0])]

# ==== Part 1 ==== #
res = 0
for i, line in enumerate(schema):
    for m in re.finditer(r'\d+', line):
        a, b = m.span()
        crop = schema[i-1][a-1:b+1] + schema[i][a-1:b+1] + schema[i+1][a-1:b+1]
        if any(not c.isdigit() and c != '.' for c in crop):
            res += int(m.group())
print(res)

# ==== Part 2 ==== #
gears = defaultdict(list)
for i, line in enumerate(schema):
    for m in re.finditer(r'\d+', line):
        a, b = m.span()
        crop = schema[i-1][a-1:b+1] + schema[i][a-1:b+1] + schema[i+1][a-1:b+1]
        if '*' in crop:
            idx = crop.index('*')
            x = a + idx % (b-a+2) - 1
            y = i + idx // (b-a+2) - 1
            gears[(x,y)].append(int(m.group()))

res = 0
for g in gears.values():
    if len(g) == 2:
        res += g[0] * g[1]
print(res)