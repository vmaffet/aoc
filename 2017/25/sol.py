#!/usr/bin/python3
import argparse
from collections import defaultdict
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

text = ''
with open(args.file, 'r') as f:
    for line in f:
        text += line
        
result = re.compile(
r"""^Begin in state (\D)\.
Perform a diagnostic checksum after (\d+) steps.\n\n""", re.MULTILINE).match(text)

state, ite = result.groups()
text = text[len(result.group(0)):]

prog = re.compile(
r"""In state (\D):
  If the current value is (\d):
    - Write the value (\d).
    - Move one slot to the (right|left).
    - Continue with state (\D).
  If the current value is (\d):
    - Write the value (\d).
    - Move one slot to the (right|left).
    - Continue with state (\D).""", re.MULTILINE)

rules = {}
while text:
    result = prog.match(text)
    s, v0, w0, m0, s0, v1, w1, m1, s1 = result.groups()
    text = text[len(result.group(0)):].strip()
    
    rules[s] = {int(v0):(int(w0), -1 if m0 == 'left' else 1, s0), int(v1):(int(w1), -1 if m1 == 'left' else 1, s1)}

tape = defaultdict(int)
position = 0
for _ in range(int(ite)):
    write, move, state = rules[state][tape[position]]
    tape[position] = write
    position += move
    
if args.part == 1:
    print(sum(tape.values()))
        
elif args.part == 2:
    pass