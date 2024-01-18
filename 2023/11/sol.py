#!/usr/bin/python3

galaxies = []
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        galaxies.extend(
            (x,y) for x, c in enumerate(line.strip()) if c == '#'
        )

allX = {x for (x,_) in galaxies}
allY = {y for (_,y) in galaxies}

maxX = max(allX)
maxY = max(allY)

emptyX = [x for x in range(maxX) if x not in allX]
emptyY = [y for y in range(maxY) if y not in allY]

def lengthsSum(k):
    length = 0
    for i, (gx, gy) in enumerate(galaxies):
        for (hx, hy) in galaxies[i+1:]:
            length += abs(hx-gx) + abs(hy-gy) \
                + (k-1) * sum(min(gx, hx) < x < max(gx, hx) for x in emptyX) \
                + (k-1) * sum(min(gy, hy) < y < max(gy, hy) for y in emptyY)
    return length

# ==== Part 1 ==== #
print(lengthsSum(2))

# ==== Part 2 ==== #
print(lengthsSum(1000000))
