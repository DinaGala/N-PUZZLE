def manhattan_distance(state, goal, size):
    dist = 0
    for index, val in enumerate(state):
        if val == 0:
            continue
        row, col = divmod(index, size)
        goal_row, goal_col = goal[val]
        dist += abs(goal_row - row) + abs(goal_col - col)
    return dist

heuristics = {
    1: manhattan_distance,
    # 2: misplaced_tiles,
    # 3: linear_conflict
}