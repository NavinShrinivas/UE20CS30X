#!/usr/bin/env python3


import sys 
import json
import math

output_map = dict()

for line in sys.stdin :
    timestamp = line.strip()
    try :
        output_map[str(timestamp)]=str(int(output_map[str(timestamp)])+1)
    except :
        output_map[str(timestamp)]=str(1)

                        
for i in sorted(output_map.keys()) : 
    if i == " " or i == "": 
        continue
    print(i, output_map[i])
