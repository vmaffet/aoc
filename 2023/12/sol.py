#!/usr/bin/python3

from functools import cache

records, sizes = [], []
with open('input.txt', 'r') as f:
    for line in f:
        record, size = line.split()
        records.append(record)
        sizes.append(tuple(map(int, size.split(','))))

@cache
def arrangements(record, groupSizes):
    if not groupSizes:
        return 1 if '#' not in record else 0

    possibleGroup0 = [
        '.'*i + '#'*groupSizes[0] + '.'
        for i in range(len(record) - sum(groupSizes) - len(groupSizes) + 1)
    ]
    matchesRecord = [
        all(r in {c,'?'} for r,c in zip(record, g0))
        for g0 in possibleGroup0
    ]
    nArrangements = sum(
        arrangements(record[len(g0):], groupSizes[1:])
        for (g0, match) in zip(possibleGroup0, matchesRecord)
        if match
    )
    return nArrangements

# ==== Part 1 ==== #
print(
    sum(
        arrangements(r+'.', s)
        for r, s in zip(records, sizes)
    )
)

# ==== Part 2 ==== #
print(
    sum(
        arrangements('?'.join([r]*5)+'.', s*5)
        for r, s in zip(records, sizes)
    )
)
