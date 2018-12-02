#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    todo = []

    with open(args.file, 'r') as f:
        todo = list(map(int, f.read().strip('\n').split(',')))
        
    n = 256
    rope = [i for i in range(n)]
    
    pos = 0
    skip = 0
    
    for l in todo:
        torev = []
        if pos + l > n:
            torev = rope[pos:] + rope[:l-(n-pos)]
        else:
            torev = rope[pos:pos+l]
        
        reved = torev[::-1]
        if pos + l > n:
            rope[pos:] = reved[:n-pos]
            rope[:l-(n-pos)] = reved[n-pos:]
        else:
            rope[pos:pos+l] = reved
        
        pos = (pos + l + skip) % n
        skip += 1
    
    print(rope[0]*rope[1])

if args.part == 2:
    
    todo = []

    with open(args.file, 'r') as f:
        todo = [ord(c) for c in f.read().strip('\n')] + [17, 31, 73, 47, 23]
        
    n = 256
    rope = [i for i in range(n)]
    
    pos = 0
    skip = 0
    for i in range(64):
        for l in todo:
            torev = []
            if pos + l > n:
                torev = rope[pos:] + rope[:l-(n-pos)]
            else:
                torev = rope[pos:pos+l]
            
            reved = torev[::-1]
            if pos + l > n:
                rope[pos:] = reved[:n-pos]
                rope[:l-(n-pos)] = reved[n-pos:]
            else:
                rope[pos:pos+l] = reved
            
            pos = (pos + l + skip) % n
            skip += 1
        
    densehash = []
    for i in range(0, n, 16):
        res = rope[i]
        for j in range(1,16):
            res ^= rope[i+j]
        densehash.append(res)
        
    hashstring = ''
    for d in densehash:
        hashstring += hex(d)[2:].zfill(2)
   
    print(hashstring)
