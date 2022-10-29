#!/usr/bin/env python3



import sys
import math
import json

old_rank = sys.argv[1]
page_embedding = sys.argv[2]

page_embed_fd = open(page_embedding, "r")
page_embedding_string = page_embed_fd.read()
try : 
    page_embedding_json = json.loads(page_embedding_string)
except : 
    exit


fd = open(old_rank, "r")
csv_string = fd.read()
rank = dict()
for line in csv_string.split("\n"):
    if line=='':
        continue
    split = line.strip().split(",")
    rank[int(split[0])] = float(split[1])
    # print(rank)
fd.close()


# Note for norm : We only have 6 elements (link) in each of our page in page_embedding, hence we dont even need a loop!
def norm_of_one(v):
    norm_v = 0.000
    v_vector = page_embedding_json[str(v)]
    norm_v+=math.pow(v_vector[0],2)
    norm_v+=math.pow(v_vector[1],2)
    norm_v+=math.pow(v_vector[2],2)
    norm_v+=math.pow(v_vector[3],2)
    norm_v+=math.pow(v_vector[4],2)
    norm_v+=math.pow(v_vector[5],2)
    return norm_v

def dot(v, w):
    v1 = page_embedding_json[str(v)]
    v2 = page_embedding_json[str(w)]
    sum = 0.000
    sum+=v1[0]*v2[0]
    sum+=v1[1]*v2[1]
    sum+=v1[2]*v2[2]
    sum+=v1[3]*v2[3]
    sum+=v1[4]*v2[4]
    sum+=v1[5]*v2[5]
    return sum

def similarity(x,p,cache):
    if cache == None:
        # Calculate both 
        cache = norm_of_one(p)
        norm_x = norm_of_one(x)
        dot_p_x = dot(p,x)
        s = dot_p_x/(cache+norm_x-dot_p_x)
        return (cache, s)
    else : 
        norm_x = norm_of_one(x)
        dot_p_x = dot(p,x)
        s = dot_p_x/(cache+norm_x-dot_p_x)
        return (cache, s)



def contribution_to_from(p,x, all_node_outgoing_from_x, cache):

    rank_of_parent_node = 0
    try : 
        rank_of_parent_node = rank[x]
    except:
        rank_of_parent_node = 0
    cache,s = similarity(p,x,cache)
    # print(rank_of_parent_node)
    c = (rank_of_parent_node*s)/len(all_node_outgoing_from_x)

    return (cache, c)



for line in sys.stdin:
    if line[0] == "#":
         continue
    cache = None
    # Cache will hold the norm of the source node 
    split = line.strip().split("\t")
    current_parent_node = int(split[0])
    current_outgoing_nodes = json.loads(split[1].strip())

    ## Task 2 doesnt seem to care about time...but a docker container will def have mem limits, hence not parsing csv 
    print(current_parent_node, 0)

    for i in current_outgoing_nodes:
        cache, c =  contribution_to_from(i,current_parent_node, current_outgoing_nodes, cache)
        print(i,c)

