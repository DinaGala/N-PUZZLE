import heapq
from .heuristics import heuristics
from .output import print_output, find_path

def a_star(heuristic, field, goal, goal_state, size):

    open_set = []  # open_set of states to explore as priority queue (heapq)
    closed_set = set()  # seen states 
    came_from = {}
    g_cost = {} #distance cost from start
    nb_state = 0 #complexity in time
    max_state = 0 #complexity in memory
    
    #init with start field
    start = field
    g_cost[start] = 0
    came_from[start] = None
    f_cost = g_cost[start] + heuristics[heuristic](start, goal, size)
    heapq.heapify(open_set)
    heapq.heappush(open_set, (f_cost, start)) #pushing start point with 0 distance and heuristic cost

    while open_set:
        f, current = heapq.heappop(open_set)
        nb_state += 1
        closed_set.add(current)
        current_memory = len(open_set) + len(closed_set)
        max_state = max(max_state, current_memory)
        if current == goal_state:
            break
        
        for neighbor in get_neighbors(current, size): #get the possibe adjacent state
            g_neighbor = g_cost[current] + 1 #only NSWE possible at cost = 1
            f_cost = g_neighbor + heuristics[heuristic](neighbor, goal, size)
            if neighbor not in closed_set or g_neighbor < g_cost.get(neighbor, float('inf')): #comparing new distance cost from current to last distance cost
                g_cost[neighbor] = g_neighbor
                heapq.heappush(open_set,(f_cost, neighbor))
                came_from[neighbor] = current
        
    print_output(find_path(came_from, current), nb_state, max_state, size)

algorithms = {
    1: a_star
}

def get_neighbors(state, size):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, size)
    # up (row), down (row), left (col), right (col), 
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size:
            new_zero = nr * size + nc
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
            # print(state)
            # print(new_state)
    return neighbors

