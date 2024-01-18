#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    raw = f.read()

rawA, rawB = raw.split("\n\n")

def recursiveSplit(x):
    s = re.split(r'[:,]', x, maxsplit=2)
    if len(s) == 1:
        return s[0]
    else:
        return ((s[0][0], s[0][1], int(s[0][2:])), s[1], recursiveSplit(s[2]))

workflows = {}
for line in rawA.split():
    (k,v), = re.findall(r'(\w+)\{(.+)\}', line)
    workflows[k] = recursiveSplit(v)

ratings = []
for line in rawB.split():
    ratings.append({k:int(v) for k,v in re.findall(r'(\w+)=(\d+)', line)})

# ==== Part 1 ==== #
op2func = {'>': lambda x,y: x>y, '<': lambda x,y: x<y}

def applyWorkflow(w, r):
    if type(w) is str:
        if w in workflows:
            w = workflows[w]
        else:
            return w
    ((cat, op, val), a, b) = w
    w = a if op2func[op](r[cat], val) else b
    return applyWorkflow(w, r)

print(
    sum(
        sum(r.values()) 
        for r in ratings 
        if applyWorkflow('in', r) == 'A'
    )
)

# ==== Part 2 ==== #
def prod(ite):
    p = 1
    for x in ite:
        p *= x
    return p

def applyWorkflowRange(w, r):
    if type(w) is str:
        if w in workflows:
            w = workflows[w]
        else:
            return prod(x[1]-x[0] for x in r.values()) if w == 'A' else 0

    ((cat, op, val), a, b) = w

    ra, rb = r.copy(), r.copy()
    ca, cb = r[cat]
    if op == '>':
        ra[cat] = (max(val+1, ca), cb)
        rb[cat] = (ca, min(val+1, cb))
    else:
        ra[cat] = (ca, min(val, cb))
        rb[cat] = (max(val, ca), cb)

    return applyWorkflowRange(a, ra) + applyWorkflowRange(b, rb)

r = {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)}
print(applyWorkflowRange('in', r))
