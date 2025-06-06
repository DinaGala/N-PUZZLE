import random
from . import macros

def parse_field(filename):

    field = []
    size = None

    with open(filename, 'r') as f:
        for line in f:
            line = line.split('#', 1)[0]
            line = line.strip()
            if not line:
                continue
            
            if size is None:
                try:
                    size = int(line)
                except ValueError:
                    raise ValueError("Board size must be an integer.")
                if size < macros.MINP or size > macros.MAXP:
                    raise ValueError(f"Board size must be between {macros.MINP} and {macros.MAXP}") 
                continue

            if size is None:
                raise ValueError("Board size is not specified.")

            try:
                row = list(map(int, line.split()))
            except ValueError:
                raise ValueError("Board rows can contain integers only.")
            if len(row) != size:
                raise ValueError(f"Board size is {size}, each row must contain {size} numbers")
            field.extend(row)
    
    
    if len(field) != size * size:
        raise ValueError(f"Board must contain exactly {size} rows.")
    if set(field) != set(range(size * size)):
        raise ValueError(f"Board must contain all numbers from 0 to {size * size - 1} without duplicates.")
    # print(field)
    return size, tuple(field)

def generate_goal(size):
    goal = [[0] * size for _ in range(size)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    for i in range(1, size * size):
        goal[x][y] = i
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < size and 0 <= ny < size and goal[nx][ny] == 0:
            x, y = nx, ny 
        else:
            d = (d + 1) % 4
            x, y = x + dx[d], y + dy[d]
    return goal

def create_goal_positions(goal):

    ''' 
    returns 2 representation of a goal state:
    - a map with target coordinates for each value and 
    - a tuple of the goal state 
    '''

    goal_pos = {}
    for i, row in enumerate(goal):
        for j, val in enumerate(row):
            goal_pos[val] = i, j
    return goal_pos, tuple(val for row in goal for val in row)
    

def generate_field(size):

    field = tuple(random.sample(range(0, size * size), size * size))
    return field