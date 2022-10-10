#!/usr/bin/env python3
import sys

for line in sys.stdin:
    words = line.lower().strip().split()
    for word in words:
        print(f"{word},1")