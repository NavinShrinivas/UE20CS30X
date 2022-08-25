"""
You can create any other helper funtions.
Do not modify the given functions
"""


"""
-1 means no path
h is given for A* search
"""

def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    """
    A* search takes the least g[n->n+1] + h[n+1] node
    """
    path = []
    current = start_point 
    while current not in goals:
        path.append(current)
        current_outgoing_g = cost[current]
        least = 9999999;
        least_next_node = 0;
        for i in range(0,len(current_outgoing_g)):
            if current_outgoing_g[i] > 0:
                temp = heuristic[i] + current_outgoing_g[i]
                if temp <= least: # Very sus, need to ask prof
                    least = temp
                    least_next_node = i
        current = least_next_node
    path.append(current) # Last goal also needs to be appended
    # TODO
    return path




def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    """
    To be able to find shortest path using DFS, we need to use IDS (Iterative deepening search)
    i.e we need to optimise at all steps
    """
    path = []
    # TODO
    return path
