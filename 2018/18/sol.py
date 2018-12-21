#!/usr/bin/python3
import argparse
import numpy as np
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
parser.add_argument("-d", "--disp", help="disp", type=bool, default=False)
args = parser.parse_args()

color = {'.':(0,0,0), '|':(61,168,31), '#':(5,75,140)} # bgr format...

area = []

with open(args.file, 'r') as f:
    for line in f:
        if line.strip():
            area.append(list(line.strip()))

area = np.array(area)
       
            
def showarea(t):
    cv2.imshow('hello', np.moveaxis(np.vectorize(color.get)(area), 0, -1).astype(np.uint8))
    cv2.waitKey(t)
    

def doite():
    global area
    limy, limx = area.shape
    changing = np.copy(area)
    for x in range(limx):
        for y in range(limy):
            if area[y, x] == '.':
                if np.count_nonzero(area[max(0,y-1):min(limy,y+2), max(0,x-1):min(limx,x+2)] == '|') >= 3:
                    changing[y, x] = '|'
            elif area[y, x] == '|':
                if np.count_nonzero(area[max(0,y-1):min(limy,y+2), max(0,x-1):min(limx,x+2)] == '#') >= 3:
                    changing[y, x] = '#'
            elif area[y, x] == '#':
                if np.count_nonzero(area[max(0,y-1):min(limy,y+2), max(0,x-1):min(limx,x+2)] == '#') == 1 \
                   or np.count_nonzero(area[max(0,y-1):min(limy,y+2), max(0,x-1):min(limx,x+2)] == '|') == 0:
                    changing[y, x] = '.'
    area = changing
    

if args.part == 1:
    for i in range(10):
        doite()
        if args.disp:
            showarea(100)
    print(np.count_nonzero(area == '|') * np.count_nonzero(area == '#'))
    
elif args.part == 2:
    save = []
    def savedat():
        for i in range(len(save)):
            if np.array_equal(area, save[i]):
                return i
        return -1
    
    while savedat() == -1:
        save.append(area)
        doite()
        if args.disp:
            showarea(100)
    
    loopstart = savedat()
    n = 1000000000
    area = save[ ((n - loopstart) % (len(save) - loopstart)) + loopstart ]
    
    print(np.count_nonzero(area == '|') * np.count_nonzero(area == '#'))
