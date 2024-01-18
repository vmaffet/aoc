#!/usr/bin/python3

from collections import deque

FlipFlop, Conjunction, Broadcast = 1, 2, 3

modtype, modstate, modin, modout = {}, {}, {}, {}
with open('input.txt', 'r') as f:
    for line in f:
        mod, out = line.strip().split(' -> ')
        if mod == 'broadcaster':
            modtype[mod] = Broadcast
        else:
            t, mod = mod[0], mod[1:]
            modtype[mod] = FlipFlop if t == '%' else Conjunction

        modstate[mod] = False

        modout[mod] = out.split(', ')
        for m in modout[mod]:
            if m not in modin:
                modin[m] = []
            modin[m].append(mod)

def pushButton(action):
    ret = False

    pulses = deque([('broadcaster', False)])
    while pulses:
        mod, lvl = pulses.popleft()

        if type(action) is dict:
            action[lvl] += 1
        elif type(action) is str:
            if mod == action and lvl:
                ret = True

        if mod not in modtype:
            continue
        t = modtype[mod]

        if t == Broadcast:
            modstate[mod] = lvl
        elif t == FlipFlop:
            if lvl:
                continue
            modstate[mod] = not modstate[mod]
        elif t == Conjunction:
            modstate[mod] = not all(modstate[m] for m in modin[mod])

        pulses.extend([(m, modstate[mod]) for m in modout[mod]])

    return ret

# ==== Part 1 ==== #
cnt = {True:0, False:0}
for _ in range(1000):
    pushButton(cnt)
print(cnt[True] * cnt[False])

# ==== Part 2 ==== #
modstate = {k:False for k in modstate}
i, n = 0, []
while True:
    i += 1
    if pushButton(modin['rx'][0]):
        n.append(i)
        if len(n) == 4:
            break

res = 1
for x in n:
    res *= x
print(res)
