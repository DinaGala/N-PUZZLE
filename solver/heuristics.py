def manhattan_distance(state, goal, size):
    dist = 0
    for index, val in enumerate(state):
        if val == 0:
            continue
        row = index // size
        col = index % size
        goal_row, goal_col = goal[val]
        dist += abs(goal_row - row) + abs(goal_col - col)
    return dist

def linear_conflict(state, goal, size):
    return manhattan_distance(state, goal, size) + count_conflicts(state, goal, size)

def count_conflicts(state, goal, size):
    conf = 0

    for r in range(size):
        max_val = -1
        for c in range(size):
            val = state[r * size + c]
            if val and goal[val][0] == r:
                if val > max_val:
                    max_val = val
                else:
                    conf += 2
    
    for c in range(size):
        max_val = -1
        for r in range(size):
            val = state[r * size + c]
            if val and goal[val][1] == c:
                if val > max_val:
                    max_val = val
                else:
                    conf += 2
    
    return conf
    

heuristics = {
    1: manhattan_distance,
    2: linear_conflict
    # 3: misplaced_tiles,
    
}