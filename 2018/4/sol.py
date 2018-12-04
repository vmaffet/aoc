#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

logs = dict()

with open(args.file, 'r') as f:
    for line in f:
        matcher = re.match(r'^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.+)$', line)
        if matcher:
            logs[matcher.group(1)] = matcher.group(2)
   
sleepRecords = dict()

for date in sorted(logs.keys()):
    matcher = re.match(r'^Guard #(\d+) begins shift$', logs[date])
    if matcher:
        guard = int(matcher.group(1))
        if guard not in sleepRecords:
            sleepRecords[guard] = [0] * 60
    else:
        matcher = re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:(\d{2})$', date)
        time = int(matcher.group(1))
        if logs[date] == 'falls asleep':
            falls = time
        elif logs[date] == 'wakes up':
            wakes = time
            for i in range(falls, wakes):
                sleepRecords[guard][i] += 1

if args.part == 1:
    best_guard = max(sleepRecords, key=lambda x:sum(sleepRecords[x]))
    
elif args.part == 2:
    best_guard = max(sleepRecords, key=lambda x:max(sleepRecords[x]))
    
probable_minute = sleepRecords[best_guard].index(max(sleepRecords[best_guard]))

print(best_guard*probable_minute)
