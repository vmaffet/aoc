#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

def knothash(s):
    todo = [ord(c) for c in s] + [17, 31, 73, 47, 23]
        
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
   
    return hashstring


key = ''
with open(args.file, 'r') as f:
    key = f.read().strip('\n')

mem_map = []

count_used = 0    
for i in range(128):
    srow = '{}-{}'.format(key, i)
    khash = knothash(srow)
    binstring = bin(int(khash, 16))[2:].zfill(4*len(khash))
    mem_map.append(list(map(int, list(binstring))))
    count_used += binstring.count('1')
        
if args.part == 1:        
    print(count_used)

if args.part == 2:
    
    
    def fill_pound(x, y, n):
        if x >= 0 and x < 128 and y >= 0 and y < 128 and mem_map[y][x] == 1:
           mem_map[y][x] = -n
           fill_pound(x+1,y  ,n)
           fill_pound(x-1,y  ,n)
           fill_pound(x  ,y+1,n)
           fill_pound(x  ,y-1,n)
    
    pound_num = 0
    for i in range(128):
        for j in range(128):
            if mem_map[j][i] == 1:
                fill_pound(i,j,pound_num)
                pound_num += 1
                
    print(pound_num)
