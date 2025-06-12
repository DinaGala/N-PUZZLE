import heapq, time
#from .heuristics import heuristics
from .output import print_output, find_path, save_to_file
#from .getneighbors import get_neighbors
from .fast_neighbors import get_neighbors
from .fast_heuristics import heuristics
from .macros import algorithm_names, heuristic_names

def a_star(heuristic, field, goal, goal_state, size, g_weight = 1, h_weight = 1):
    """
    Implements the A* search algorithm to find the shortest path from the initial puzzle state to the goal.
    A* uses a cost function f(n) = g(n) + h(n), where:
    - g(n) is the cost to reach node n from the start (actual cost),
    - h(n) is the estimated cost from node n to the goal (heuristic).

    Steps:
    1. Initialize the following data structures:
       - `open_set`: a priority queue containing nodes to explore, ordered by their f-costs.
       - `closed_set`: a set of already-explored nodes.
       - `g_cost`: maps each state to the cost of reaching it from the start.
       - `came_from`: maps each node to its predecessor (for path reconstruction).
       - `open_set_lookup`: mirrors the open set, allowing for efficient f-cost comparison.
       - `nb_state`, `max_state`: track time and space complexity.

    2. Begin with the initial state:
       - Set g = 0 and compute its f = g + h.
       - Add it to the priority queue.

    3. Main loop:
       - Pop the node with the lowest f-cost from the open set.
       - Mark it as visited and update memory tracking.
       - If this node is the goal, exit the loop.

    4. For each neighbor of the current node:
       - Skip it if already visited.
       - Compute tentative g and f costs.
       - If this path to the neighbor is better than any previously recorded:
           - Update its g-cost and path.
           - Add it to the open set if it's not already scheduled, or if it now has a better f-cost.

    5. Continue until the goal state is reached or the open set is exhausted.

    Finally, the algorithm prints:
    - Number of moves to reach the goal.
    - Number of states expanded (time complexity).
    - Maximum states in memory at any point (space complexity).
    - The full solution path from start to goal.
    """
    start_time = time.time()
    open_set = []  # open_set of states to explore as priority queue (heapq)
    closed_set = set()  # seen states 
    came_from = {} #path of visited node
    open_set_lookup = {}
    g_cost = {} #distance cost from start
    nb_state = 0 #complexity in time
    max_state = 0 #complexity in memory
    
    #init with start field
    start = field
    g_cost[start] = 0
    came_from[start] = None
    f_cost = g_cost[start] * g_weight + heuristics[heuristic](start, goal, size, goal_state) * h_weight
    heapq.heapify(open_set)
    heapq.heappush(open_set, (f_cost, start)) #pushing start point with 0 distance and heuristic cost

    while open_set:
        f, current = heapq.heappop(open_set)
        nb_state += 1
        closed_set.add(current)
        current_memory = len(open_set_lookup) + len(closed_set)
        max_state = max(max_state, current_memory)
        
        if current == goal_state:
            end_time = time.time()
            break

        #get the possibe adjacent states
        for neighbor in get_neighbors(current, size):
            
            #if the neighbor was visited as current state previously, we don't explore it
            if neighbor in closed_set:
                continue
            #compute f = g + h with g = only NSWE possible at cost = 1, h = heuristic function
            g_neighbor = g_cost[current] + 1 
            f_neighbor = g_neighbor * g_weight + heuristics[heuristic](neighbor, goal, size, goal_state) * h_weight
            
            #look if the g_cost for neighbor needs to be udpated (and therefore path to it as well)
            if neighbor not in g_cost or g_neighbor < g_cost[neighbor]: #comparing new distance cost from current to last distance cost
                g_cost[neighbor] = g_neighbor
                came_from[neighbor] = current
                
                #look if neighbor needs to be added to the queue (not present ye or lower f cost)
                if neighbor not in open_set_lookup or f_neighbor < open_set_lookup[neighbor]:
                    heapq.heappush(open_set,(f_neighbor, neighbor))
                    open_set_lookup[neighbor] = f_neighbor
    
    elapsed_time = end_time - start_time
    if h_weight + g_weight == 2:
        algo = 1
    elif g_weight == 1:
        algo = 2
    else:
        algo = 3
    msg = f"🧩 Chosen algorithm: {algorithm_names[algo]}, chosen heristic: {heuristic_names[heuristic]}"                
    print_output(find_path(came_from, current), nb_state, max_state, size, elapsed_time, msg)

def uniform_cost(heuristic, field, goal, goal_state, size):
    return a_star(heuristic, field, goal, goal_state, size, g_weight = 1, h_weight = 0)

def greedy_search(heuristic, field, goal, goal_state, size):
    return a_star(heuristic, field, goal, goal_state, size, g_weight=0, h_weight=1)

algorithms = {
    1: a_star,          # A* (default g=1, h=1)
    2: uniform_cost,    # UCS (g=1, h=0)
    3: greedy_search    # Greedy (g=0, h=1)
}


