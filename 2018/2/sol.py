#!/usr/bin/python3
import argparse
import difflib

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    count2 = 0
    count3 = 0

    with open(args.file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line:
                good2 = False
                good3 = False
                for c in line:
                    count = line.count(c)
                    if count == 2:
                        good2 = True
                    elif count == 3:
                        good3 = True
                if good2:
                    count2 += 1
                if good3:
                    count3 += 1

    print(count2*count3)
    
elif args.part == 2:
    
    base = []

    with open(args.file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line:
                for old in base:
                    matching = ''
                    for df in difflib.ndiff(line, old):
                        if df[0] == ' ':
                            matching += df.strip(' ')
                    if len(matching) == len(line)-1:
                        print(matching)
                        exit()
                base.append(line)

