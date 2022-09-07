#!/usr/bin/python
import sys
import json
import datetime
import time

wordCount = dict()

for line in sys.stdin:
    line = line.strip()
    date,count = line.split("\t")
    date=date.strip()
    try:
        count = int(count.strip())
    except:
        continue
    if date not in wordCount.keys():
        wordCount[date] = 0
    wordCount[date]+= count
items = list(wordCount.items())
items.sort(key = lambda x: x[0])
for date,count in items:
    print(f"{date} {count}")
