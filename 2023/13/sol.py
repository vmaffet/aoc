#!/usr/bin/python3

with open('input.txt', 'r') as f:
    patterns = [pat.split() for pat in f.read().split('\n\n')]

def transpose(arr):
    return [''.join(row[i] for row in arr) for i in range(len(arr[0]))]

# ==== Part 1 ==== #
def findReflection(arr):
    for i in range(len(arr)-1):
        if all(a == b for a, b in zip(arr[i::-1], arr[i+1:])):
            return i+1
    return 0

res = 0
for pat in patterns:
    val = 100 * findReflection(pat)
    if not val:
        val = findReflection(transpose(pat))
    res += val
print(res)

# ==== Part 2 ==== #
def diff(a, b):
    return sum(ca != cb for ca, cb in zip(a, b))

def findSmudgeReflection(arr):
    for i in range(len(arr)-1):
        if sum(diff(a, b) for a, b in zip(arr[i::-1], arr[i+1:])) == 1:
            return i+1
    return 0

res = 0
for pat in patterns:
    val = 100 * findSmudgeReflection(pat)
    if not val:
        val = findSmudgeReflection(transpose(pat))
    res += val
print(res)
