#!/usr/bin/python3
import argparse
import re
import numpy as np
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
parser.add_argument("-d", "--disp", help="disp", type=bool, default=False)
args = parser.parse_args()

color = {'.':(0,0,0), '#':(255,255,255), '~':(255,0,0), '|':(51,102,153), '+':(0,0,255)} # bgr format...

scans = []
limits = {'max':{'x':0, 'y':0}, 'min':{'x':float('inf'), 'y':float('inf')}}

with open(args.file, 'r') as f:
    for line in f:
        if line.strip():
            matcher = re.match(r'(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)', line)
            if matcher:
                a, b, c, d, e = matcher.groups()
                b, d, e = int(b), int(d), int(e)
                limits['min'][a] = min(limits['min'][a], b)
                limits['max'][a] = max(limits['max'][a], b)
                limits['min'][c] = min(limits['min'][c], d)
                limits['max'][c] = max(limits['max'][c], e)
                scans.append([a, b, c, d, e])
        
limits['min']['x'] -= 5
limits['max']['x'] += 5
limits['min']['y'] -= 5
limits['max']['y'] += 5

startx = 500 - limits['min']['x']

soil = np.full((limits['max']['y'] - limits['min']['y']+1, limits['max']['x'] - limits['min']['x']+1), '.')
soil[limits['min']['y'] + 4, startx] = '+'
for i in range(len(scans)):
    a, b, c, d, e = scans[i]
    scans[i] = [a, b-limits['min'][a], c, d-limits['min'][c], e-limits['min'][c]]
    if scans[i][0] == 'x':
        for k in range(scans[i][3], scans[i][4]+1):
            soil[k, scans[i][1]] = '#'
    else:
        for k in range(scans[i][3], scans[i][4]+1):
            soil[scans[i][1], k] = '#'
            
def showsoil(t):
    cv2.imshow('hello', np.moveaxis(np.vectorize(color.get)(soil), 0, -1).astype(np.uint8))
    cv2.waitKey(t)
    

def walls(x, y):
    lx = x
    while soil[y, lx] != '#':
        lx -= 1
        if lx < 0 or soil[y+1, lx] not in '~#':
            lx = None
            break
    rx = x
    while soil[y, rx] != '#':
        rx += 1
        if rx >= soil.shape[1] or soil[y+1, rx] not in '~#':
            rx = None
            break
    return lx, rx
    
    
def edges(x, y):
    lx = x
    while soil[y, lx] != '#' and soil[y+1, lx] in '~#':
        lx -= 1
    rx = x
    while soil[y, rx] != '#' and soil[y+1, rx] in '~#':
        rx += 1
    return lx, rx
    

def depth(x, y):
    by = y
    while by < soil.shape[0] and soil[by, x] in '.|':
        by += 1
    return by
    

toprocess = [(startx, limits['min']['y'] + 5)]
while toprocess:
    px, py = toprocess.pop(0)
    if py != limits['max']['y']:
        if soil[py+1, px] in '.|':
            by = depth(px, py+1)
            soil[py:by, px] = np.full((by-py), '|')
            if (px, by-1) not in toprocess:
                toprocess.append((px, by-1))
        elif soil[py+1, px] in '~#':
            lx, rx = walls(px, py)
            if lx is not None and rx is not None:
                soil[py, lx+1:rx] = np.full((rx-lx-1), '~')
                if (px, py-1) not in toprocess:
                    toprocess.append((px, py-1))
            else:
                lx, rx = edges(px, py)
                soil[py, lx+1:rx] = np.full((rx-lx-1), '|')
                if soil[py, lx] != '#':
                    soil[py, lx] = '|'
                    if (lx, py) not in toprocess:
                        toprocess.append((lx, py))
                if soil[py, rx] != '#':
                    soil[py, rx] = '|'
                    if (rx, py) not in toprocess:
                        toprocess.append((rx, py))
        if args.disp:    
            showsoil(1)

cv2.imwrite('final.png',np.moveaxis(np.vectorize(color.get)(soil[:limits['max']['y']-4, :]), 0, -1).astype(np.uint8))

if args.part == 1:
    print(np.count_nonzero(soil[:limits['max']['y']-4, :] == '~') + np.count_nonzero(soil[:limits['max']['y']-4, :] == '|'))

elif args.part == 2:
    print(np.count_nonzero(soil[:limits['max']['y']-4, :] == '~'))
