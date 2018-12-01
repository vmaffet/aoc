#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    checksum = 0

    with open(args.file, 'r') as f:
        for line in f:
            if line.strip('\n'):
                nums = list(map(int, line.strip('\n').split('\t')))
                checksum += max(nums) - min(nums)
    
    print(checksum)
    
elif args.part == 2:
    
    checksum = 0

    with open(args.file, 'r') as f:
        for line in f:
            if line.strip('\n'):
                nums = list(map(int, line.strip('\n').split('\t')))
                for i in range(len(nums)):
                    for j in range(len(nums)):
                        if j != i and nums[j] % nums[i] == 0:
                            checksum += int(nums[j]/nums[i])
    
    print(checksum)
