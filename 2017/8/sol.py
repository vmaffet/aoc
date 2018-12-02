#!/usr/bin/python3
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()


variables = defaultdict(lambda:0, dict())
alltimemax = 0

with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match(r'^(\w+) (\w+) (-?\d+) if (\w+) (\W+) (-?\d+)$', line)
        if matcher:
            op_var = matcher.group(1)
            op = matcher.group(2)
            op_val = int(matcher.group(3))
            test_var = matcher.group(4)
            test = matcher.group(5)
            test_val = int(matcher.group(6))
            
            validTest = False
            if test == '==':
                validTest = variables[test_var] == test_val
            elif test == '!=':
                validTest = variables[test_var] != test_val
            elif test == '>':
                validTest = variables[test_var] > test_val
            elif test == '>=':
                validTest = variables[test_var] >= test_val
            elif test == '<':
                validTest = variables[test_var] < test_val
            elif test == '<=':
                validTest = variables[test_var] <= test_val
                
            if validTest:
                if op == 'inc':
                    variables[op_var] += op_val
                elif op == 'dec':
                    variables[op_var] -= op_val
            if variables[op_var] > alltimemax:
                alltimemax = variables[op_var]

if args.part == 1:
    print(max(variables.values()))

if args.part == 2:
    print(alltimemax)
