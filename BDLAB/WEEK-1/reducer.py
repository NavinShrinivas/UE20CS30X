#!/usr/bin/env python3
import sys

query_word = sys.argv[1]
total_count = 0
for line in sys.stdin:
    line = line.strip()
    word, count = line.rsplit(",", 1)
    count = int(count)
    if query_word == word:
        total_count += 1
print(total_count)