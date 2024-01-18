#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    durations = list(map(int, re.findall(r'\d+', f.readline())))
    records = list(map(int, re.findall(r'\d+', f.readline())))

# ==== Part 1 ==== #
res = 1
for time, dist in zip(durations, records):
    res *= sum(hold*(time-hold) > dist for hold in range(time+1))
print(res)

# ==== Part 2 ==== #
time = int(''.join(map(str, durations)))
dist = int(''.join(map(str, records)))

a, b, c = -1, time, -dist
delta = b**2 - 4*a*c
x0 = (-b + delta**0.5) / (2*a)
x1 = (-b - delta**0.5) / (2*a)
print(int(x1) - int(x0))
