#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()        

class LinkedLoop:
    def __init__(self, val, after=None):
        self.val = val
        self.prev = after or self
        self.nxt = None
        self.nxt = self.prev.nxt or self
        self.nxt.prev = self
        self.prev.nxt = self

    def delete(self):
        self.nxt.prev = self.prev
        self.prev.nxt = self.nxt
        return self.val
        
with open(args.file, 'r') as f:
    matcher = re.match(r'^(\d+) players; last marble is worth (\d+) points$', f.read().strip())
    if matcher:
        players, lastmarble = list(map(int, matcher.groups()))
       
if args.part == 2:
    lastmarble *= 100       

scores = [0] * players
board = LinkedLoop(0)
for i in range(1, lastmarble+1):
    if i % 23 == 0:
        # thank you @MathisHammel
        board = board.prev.prev.prev.prev.prev.prev
        scores[i%players] += board.prev.delete() + i
    else:
        board = LinkedLoop(i, board.nxt)

print(max(scores))        
