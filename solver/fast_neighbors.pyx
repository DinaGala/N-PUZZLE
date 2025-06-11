# neighbors.pyx

cpdef list get_neighbors(tuple state, int size):
    cdef list neighbors = []
    cdef int zero = state.index(0)
    cdef int row = zero // size
    cdef int col = zero % size
    cdef int dr, dc, nr, nc, new_zero
    cdef list new_state

    cdef int moves[4][2]
    moves[0][0], moves[0][1] = -1, 0  # Up
    moves[1][0], moves[1][1] = 1, 0   # Down
    moves[2][0], moves[2][1] = 0, -1  # Left
    moves[3][0], moves[3][1] = 0, 1   # Right

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size:
            new_zero = nr * size + nc
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))

    return neighbors
