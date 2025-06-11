# solver/heuristics.pyx

cpdef int manhattan_distance(tuple state, dict goal, int size, tuple flat_goal):
    cdef int dist = 0
    cdef int index, val, row, col, goal_row, goal_col
    for index, val in enumerate(state):
        if val == 0:
            continue
        row = index // size
        col = index % size
        goal_row, goal_col = goal[val]
        dist += abs(goal_row - row) + abs(goal_col - col)
    return dist


cpdef int count_conflicts(tuple state, dict goal, int size):
    cdef int conf = 0
    cdef int r, c, val, max_val

    for r in range(size):
        max_val = -1
        for c in range(size):
            val = state[r * size + c]
            if val == 0 or goal[val][0] != r:
                continue
            if val > max_val:
                max_val = val
            else:
                conf += 2

    for c in range(size):
        max_val = -1
        for r in range(size):
            val = state[r * size + c]
            if val == 0 or goal[val][1] != c:
                continue
            if val > max_val:
                max_val = val
            else:
                conf += 2

    return conf


cpdef int linear_conflict(tuple state, dict goal, int size, tuple flat_goal):
    return manhattan_distance(state, goal, size, flat_goal) + count_conflicts(state, goal, size)


cpdef int misplaced_tiles(tuple state, dict goal, int size, tuple flat_goal):
    cdef int i, val, count = 0
    for i in range(size * size):
        val = state[i]
        if val != 0 and val != flat_goal[i]:
            count += 1
    return count


cpdef int no_heuristic(tuple state, dict goal, int size, tuple flat_goal):
    return 0
