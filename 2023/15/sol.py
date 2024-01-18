#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    init = f.read().split(',')

def HASH(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val

# ==== Part 1 ==== #
print(sum(HASH(inst) for inst in init))

# ==== Part 2 ==== #
boxes = [{} for _ in range(256)]
for inst in init:
    [label] = re.findall(r'[a-z]+', inst)
    box = HASH(label)
    if inst.endswith('-'):
        boxes[box].pop(label, None)
    else:
        boxes[box][label] = inst[-1]

print(
    sum(
        (i+1) * (j+1) * int(focal)
        for i, box in enumerate(boxes) for j, focal in enumerate(box.values())
    )
)
