#!/usr/bin/env python3

import sys


for line in sys.stdin:
    if line[0] == "#":
        pass
    else : 
        # '#' only occur in starting of file
        print(line.replace("\t"," "), end="")
        for i in sys.stdin:
            print(i.replace("\t", ' '), end="")



# Intial grouping
# for line in sys.stdin:
#         print(line, end="")
#

#
# statefull_parent_node = "-1"
# for line in sys.stdin:
#     if line[0] == "#":
#         continue
#     split = line.strip().split("\t")
#     current_parent_node = split[0]
#     current_outgoing_node = split[1]
#     if statefull_parent_node == "-1":
#         statefull_parent_node = current_parent_node
#         print(statefull_parent_node,"\t",current_outgoing_node, sep="", end="")
#     elif statefull_parent_node != current_parent_node : 
#         print("\n", sep = "", end="")
#         statefull_parent_node = current_parent_node
#         print(statefull_parent_node,"\t",current_outgoing_node, sep="", end="")
#     else:
#         print(", ",current_outgoing_node, sep = "", end="")



# statefull_parent_node = "-1"
# temp_list = []
# for line in sys.stdin:
#     if line[0] == "#":
#          continue
#     split = line.strip().split("\t")
#     current_parent_node = split[0]
#     current_outgoing_node = split[1]
#     if statefull_parent_node == "-1":
#         statefull_parent_node = current_parent_node 
#         temp_list.append(int(current_outgoing_node))
#     elif statefull_parent_node!=current_parent_node:
#         print(int(statefull_parent_node),"\t",temp_list, sep="")
#         statefull_parent_node = current_parent_node 
#         temp_list = []
#         temp_list.append(int(current_outgoing_node))
#     else:
#         temp_list.append(int(current_outgoing_node))
# print(int(statefull_parent_node),"\t",temp_list, sep="") # For last parent node



# for line in sys.stdin:
#     if line[0] == "#":
#         continue
#     p = line.strip().split()
#     print(int(p[0]),",", int(p[1]), sep="")
