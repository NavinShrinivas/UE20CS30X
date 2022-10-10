#!/usr/bin/env python3
import sys


stateful_var = -1
temp_contrib = 0.0
for line in sys.stdin:
    split = line.strip().split(" ")
    current_to_contrib_node = int(split[0])
    contribution_to_node = float(split[1].strip())
    if stateful_var == -1:
        stateful_var = current_to_contrib_node
        temp_contrib = contribution_to_node
    elif stateful_var != current_to_contrib_node : 
        rank = 0.34 + (0.57*temp_contrib)
        print(stateful_var,",",round(rank,2), sep="")
        stateful_var = current_to_contrib_node
        temp_contrib = contribution_to_node
    else:
        temp_contrib += contribution_to_node


rank = 0.34 + (0.57*temp_contrib)
print(stateful_var,",",round(rank,2), sep="") # Last rank
