#!/usr/bin/python3
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

class Node:
    
    def __init__(self, name):
        self.name = name
        self.childs = []
        self.metadata = []
        self.value = None
        
    def addMetadata(self, md):
        self.metadata.append(md)
        
    def addChild(self, child):
        self.childs.append(child)
    
    def getValue(self):
        if self.value is None:
            self.value = 0
            if self.childs:
                for md in self.metadata:
                    if md > 0 and md <= len(self.childs):
                       self.value += self.childs[md-1].getValue()
            else:
                self.value = sum(self.metadata)
        return self.value


def extractNode(rep, x):
    nbC = rep.pop(0)
    nbM = rep.pop(0)
    nd = Node(x)
    for i in range(nbC):
        x += 1
        c, x = extractNode(rep, x)
        nd.addChild(c)
    for i in range(nbM):
        nd.addMetadata(rep.pop(0))
    return (nd, x)

with open(args.file, 'r') as f:
    license_file = list(map(int, f.read().strip().split()))

top, nbNodes = extractNode(license_file, 0)

if args.part == 1:
    
    metasum = 0
    todo = {top}
    while todo:
        nd = todo.pop()
        metasum += sum(nd.metadata)
        todo.update(nd.childs)
        
    print(metasum)

elif args.part == 2:
    print(top.getValue())
        
