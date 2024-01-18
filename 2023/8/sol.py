#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    inst = f.readline().strip()

    f.readline()
    net = {}
    for line in f:
        S, L, R = re.findall(r'[0-9A-Z]+', line)
        net[S] = (L, R)

# ==== Part 1 ==== #
i, n = 0, 'AAA'
while n != 'ZZZ':
    n, i = net[n][inst[i % len(inst)] == 'R'], i+1
print(i)

# ==== Part 2 ==== #
starts = [n for n in net.keys() if n.endswith('A')]
periods = []
for n in starts:
    i = 0
    history = {}
    while (n, i) not in history:
        history[(n, i)] = None
        n, i = net[n][inst[i] == 'R'], (i+1) % len(inst)
    periods.append(len(history) - list(history.keys()).index((n, i)))

def gcd(a, b):
    d = 1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            d = i
    return d

def gcdN(arr):
    d = arr[0]
    for x in arr:
        d = gcd(d, x)
    return d

g = gcdN(periods)
res = g
for p in periods:
    res *= p // g
print(res)
