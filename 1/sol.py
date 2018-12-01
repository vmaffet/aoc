#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    res = 0
    with open(args.file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line:
                res += int(line)
    print(res)
    
elif args.part == 2:
    
    res = 0
    seen = {res}
    while True:
        with open(args.file, 'r') as f:
            for line in f:
                line = line.strip('\n')
                if line:
                    res += int(line)
                    if res in seen:
                        print(res)
                        exit()
                    else:
                        seen.add(res)
