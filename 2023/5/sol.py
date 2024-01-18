#!/usr/bin/python3

import re

def readMap(file):
    m = []
    line = file.readline()
    while line.strip():
        m.append(tuple(map(int, line.split())))
        line = file.readline()
    return m

with open('input.txt', 'r') as f:
    seeds = list(map(int, re.findall(r'\d+', f.readline())))

    f.readline()

    maps = []
    while f.readline().strip():
        maps.append(readMap(f))

# ==== Part 1 ==== #
def applyMap(value, m):
    for d, s, n in m:
        if s <= value < s+n:
            return d + value - s
    return value

def applyMaps(value):
    for m in maps:
        value = applyMap(value, m)
    return value

print(min(map(applyMaps, seeds)))

# ==== Part 2 ==== #
def applyMapRange(a, b, m):
    for d, s, n in m:
        if s <= a and b <= s+n:
            return [(d+a-s, d+b-s)]
        elif a < s and s < b <= s+n:
            return applyMapRange(a, s, m) + [(d, d+b-s)]
        elif s <= a < s+n and s+n < b:
            return [(d+a-s, d+n)] + applyMapRange(s+n, b, m)
        elif a < s and s+n < b:
            return applyMapRange(a, s, m) + [(d, d+n)] + applyMapRange(s+n, b, m)
    return [(a, b)]

def applyMapsRange(a, b):
    ranges = [(a, b)]
    for m in maps:
        newRanges = []
        for a, b in ranges:
            newRanges.extend(applyMapRange(a, b, m))
        ranges = newRanges
    return ranges

res = min(
    min(applyMapsRange(s, s+n))
    for s, n in zip(seeds[0::2], seeds[1::2])
)[0]
print(res)
