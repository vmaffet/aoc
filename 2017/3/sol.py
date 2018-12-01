#!/usr/bin/python3
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("n", help="your number", type=int)
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

if args.part == 1:
    
    n = args.n
    m = 1
    r = 0

    while m < n:
       r += 1
       m += 8*r

    x, y = r, -r

    if n <= m - 2*r:
        m -= 2*r
        x -= 2*r
        if n <= m - 2*r:
            m -= 2*r
            y += 2*r
            if n <= m - 2*r:
                m -= 2*r
                x += 2*r
                y -= m - n
            else:
                x += m - n
        else:
            y += m - n 
    else:
        x -= m - n

    print(abs(x) + abs(y))
    
elif args.part == 2:
    
    n = args.n
    x, y = 1, 0
    res = 1
    val = {(0,0):1, (1,0):1}
    val = defaultdict(lambda:0, val)
    while res < n:
        if y < 0 and x >= y  and x <= -y:
            x += 1
        elif x > 0 and y < x:
            y += 1
        elif y > 0 and x > -y:
            x -= 1
        elif x < 0 and y > x:
            y -= 1

        res = val[(x-1, y+1)] \
             + val[(x  , y+1)] \
             + val[(x+1, y+1)] \
             + val[(x-1, y  )] \
             + val[(x+1, y  )] \
             + val[(x-1, y-1)] \
             + val[(x  , y-1)] \
             + val[(x+1, y-1)]

        val[(x,y)] = res
        #print(res)
        
    print(res)
    
