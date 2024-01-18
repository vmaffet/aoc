#!/usr/bin/python3

from collections import Counter

bids = {}
with open('input.txt', 'r') as f:
    for line in f:
        h, b = line.split()
        bids[h] = int(b)

def handtype(h, joker):
    c = Counter(h)
    unique, most = len(c), max(c.values())

    if joker and 'J' in c and unique > 1:
        unique -= 1
        if most == c['J']:
            _, second_most = [v for (_,v) in c.most_common(2)]
            most += second_most
        else:
            most += c['J']

    if unique == 1:
        return 1 # Five of a kind
    elif unique == 2:
        if most == 4:
            return 2 # Four of a kind
        else:
            return 3 # Full house
    elif unique == 3:
        if most == 3:
            return 4 # Three of a kind
        else:
            return 5 # Two pairs
    elif unique == 4:
        return 6 # One pair
    else:
        return 7 # High card

# ==== Part 1 ==== #
def handkey(h):
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    return (handtype(h, False), [order.index(c) for c in h])

strength = sorted(bids, key=handkey, reverse=True)
print(sum(bids[h] * (i+1) for i, h in enumerate(strength)))

# ==== Part 2 ==== #
def handkey2(h):
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    return (handtype(h, True), [order.index(c) for c in h])

strength = sorted(bids, key=handkey2, reverse=True)
print(sum(bids[h] * (i+1) for i, h in enumerate(strength)))

