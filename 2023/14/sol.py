#!/usr/bin/python3

with open('input.txt', 'r') as f:
    rocks = [list(line.strip()) for line in f]

def transpose(arr):
    return [[row[i] for row in arr] for i in range(len(arr[0]))]

def tilt(row):
    lock = 0
    for i, c in enumerate(row):
        if c == '#':
            lock = i+1
        elif c == 'O':
            row[lock], row[i] = 'O', row[lock]
            lock += 1
    return row

def load(arr):
    return sum(len(row) - i for row in arr for i, c in enumerate(row) if c == 'O')

# ==== Part 1 ==== #
print(load(tilt(r) for r in transpose(rocks)))

# ==== Part 2 ==== #
def flipY(arr):
    return arr[::-1]

def rotateClock(arr):
    return transpose(flipY(arr))

def cycle(arr):
    for _ in range(4):
        arr = rotateClock([tilt(row) for row in arr])
    return arr

def hashList(arr):
    return hash(tuple(tuple(row) for row in arr))

rocks = rotateClock(rotateClock(rotateClock(rocks)))

N = 1000000000
history = []
for _ in range(N):
    rocks = cycle(rocks)
    h, l = hashList(rocks), load(rocks)
    if (h, l) in history:
        break
    history.append((h, l))

start = history.index((h, l))
idx = start + (N - 1 - start) % (len(history) - start)
print(history[idx][1])
