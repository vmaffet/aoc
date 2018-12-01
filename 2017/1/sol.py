#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    captcha = ''

    with open(args.file, 'r') as f:
        captcha = f.read().strip('\n')
    
    size = len(captcha)
    res = 0    
    for i in range(size):
        if captcha[i] == captcha[(i+1)%size]:
            res += int(captcha[i])
    print(res)
    
elif args.part == 2:
    
    captcha = ''

    with open(args.file, 'r') as f:
        captcha = f.read().strip('\n')
    
    size = len(captcha)
    res = 0    
    for i in range(size):
        if captcha[i] == captcha[(i+int(size/2))%size]:
            res += int(captcha[i])
    print(res)
