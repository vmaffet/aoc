#!/usr/bin/python3

import re

# ==== Part 1 ==== #
res = 0
with open('input.txt', 'r') as f:
    for line in f:
        m = re.findall(r'\d', line)
        res += int(m[0] + m[-1])
print(res)

# ==== Part 2 ==== #
res = 0
with open('input.txt', 'r') as f:
    for line in f:
        n = 'one|two|three|four|five|six|seven|eight|nine'
        ite = list(re.finditer(f'(?=(\\d|{n}))', line))
        a, b = ite[0].group(1), ite[-1].group(1)
        text2digit = lambda x: str(n.split('|').index(x)+1) if x in n else x
        res += int(text2digit(a) + text2digit(b))
print(res)
