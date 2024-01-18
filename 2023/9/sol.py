#!/usr/bin/python3

values = []
with open('input.txt', 'r') as f:
    for line in f:
        values.append(list(map(int, line.split())))

def diff(h):
    return [y1 - y0 for y0, y1 in zip(h[:-1], h[1:])]

preceding, following = [], []
for hist in values:
    first, last = [], []
    while not all(x == 0 for x in hist):
        first.append(hist[0])
        last.append(hist[-1])
        hist = diff(hist)
    preceding.append(sum(first[0::2]) - sum(first[1::2]))
    following.append(sum(last))

# ==== Part 1 ==== #
print(sum(following))

# ==== Part 2 ==== #
print(sum(preceding))
