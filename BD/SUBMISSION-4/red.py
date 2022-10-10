#!/usr/bin/env python3

# The shuffle/sort is the only this we are doing after map, hence we have reached max concurrency

import sys
import json


# rank_vector_path = sys.argv[1]
#
# output = ""
# statefull_parent_node = "-1"
# total_nodes = 0;
# temp_list = []
# for line in sys.stdin:
#     split = line.strip().split("\t")
#     current_parent_node = split[0]
#     current_outgoing_node = json.loads(split[1])
#     if statefull_parent_node == "-1":
#         statefull_parent_node = current_parent_node
#         temp_list = current_outgoing_node
#     elif statefull_parent_node != current_parent_node : 
#         print(int(statefull_parent_node),"\t",temp_list,sep="")
#         output += statefull_parent_node+","+"1"+"\n"
#         statefull_parent_node = current_parent_node
#         temp_list = current_outgoing_node
#     else:
#         temp_list.extend(current_outgoing_node)
#
# ## last node : 
# if statefull_parent_node == "-1":
#     pass
# else:
#     print(int(statefull_parent_node),"\t",temp_list,sep="")
#     output += statefull_parent_node+","+"1"+"\n"
#
# fd = open(rank_vector_path, "w+")
# fd.write(output)
# fd.close()

rank_vector_path = sys.argv[1]
fd = open(rank_vector_path, "w+")
statefull_parent_node = "-1"
for line in sys.stdin:
    current_parent_node = line.strip().split()[0]
    current_outgoing_node = line.strip().split()[1]
    if statefull_parent_node == "-1":
        statefull_parent_node = current_parent_node
        print(statefull_parent_node,"\t","[",current_outgoing_node, sep="", end="")
    elif statefull_parent_node != current_parent_node : 
        print("]\n", sep = "", end="")
        temp = statefull_parent_node+","+"1"+"\n"
        fd.write(temp)
        statefull_parent_node = current_parent_node
        print(statefull_parent_node,"\t","[",current_outgoing_node, sep="", end="")
    else:
        print(", ",current_outgoing_node, sep = "", end="")

print("]", end="")
temp = statefull_parent_node+","+"1"+"\n"
fd.write(temp)

fd.close()
#
# for i in sys.stdin:
#     print(i)


# rank_vector_path = sys.argv[1]
#
# output = ""
# statefull_parent_node = "-1"
# total_nodes = 0;
# temp_list = []
# for line in sys.stdin:
#     split = line.strip().split(" ")
#     current_parent_node = split[0]
#     current_outgoing_node = int(split[1])
#     if statefull_parent_node == "-1":
#         statefull_parent_node = current_parent_node
#         temp_list = []
#         temp_list.append(current_outgoing_node)
#     elif statefull_parent_node != current_parent_node : 
#         print(int(statefull_parent_node),"\t",temp_list,sep="")
#         output += statefull_parent_node+","+"1"+"\n"
#         statefull_parent_node = current_parent_node
#         temp_list = []
#         temp_list.append(current_outgoing_node)
#
#     else:
#         temp_list.append(current_outgoing_node)
#
# ## last node : 
# if statefull_parent_node == "-1":
#     pass
# else:
#     print(int(statefull_parent_node),"\t",temp_list,sep="")
#     output += statefull_parent_node+","+"1"+"\n"
#
# fd = open(rank_vector_path, "w+")
# fd.write(output)
# fd.close()













