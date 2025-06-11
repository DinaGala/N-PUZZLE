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