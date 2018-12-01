#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    valid_count = 0

    with open(args.file, 'r') as f:
        for line in f:
            if line.strip('\n'):
                words = line.strip('\n').split(' ')
                base = set()
                good = True
                for w in words:
                    if w not in base:
                        base.add(w)
                    else:
                        good = False
                        break
                if good:
                    valid_count += 1

    print(valid_count)
    
elif args.part == 2:
    
    valid_count = 0

    with open(args.file, 'r') as f:
        for line in f:
            if line.strip('\n'):
                words = line.strip('\n').split(' ')
                base = set()
                good = True
                for w in words:
                    s = ''.join(sorted(w))
                    if s not in base:
                        base.add(s)
                    else:
                        good = False
                        break
                if good:
                    valid_count += 1

    print(valid_count)
