#!/usr/bin/python3

from collections import defaultdict
import re

cards = []
with open('input.txt', 'r') as f:
    for line in f:
        a, b = re.findall(r'Card\s+\d+:(.+)\|(.+)', line)[0]
        cards.append((set(map(int, a.split())), list(map(int, b.split()))))

# ==== Part 1 ==== #
res = 0
for win, nums in cards:
    v = sum(1 for n in nums if n in win)
    res += 2**(v-1) if v > 0 else 0
print(res)

# ==== Part 2 ==== #
cnt = defaultdict(int)
for i, (win, nums) in enumerate(cards):
    cnt[i] += 1
    v = sum(1 for n in nums if n in win)
    for j in range(v):
        cnt[i+1+j] += cnt[i]
print(sum(cnt.values()))
