import sys
import random
import signal
import heapq

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RES = "\033[0m"
BOLD = "\033[1m"
MINP = 2
MAXP = 9
MSG_PZL_SIZE = f"{GREEN}Choose the size of the puzzle (from {MINP} to {MAXP}):  {RES}"
MSG_ALGO = f"{BLUE}1. A*\n2.Uniform-cost\n3.Greedy search{RES}\n{GREEN}Choose the algorithm:  {RES}"
MSG_HEURISTIC = f"{BLUE}1. Manhattan-distance\n2. Linear conflict\n3. ...{RES}\n{GREEN}Choose the heuristic:  {RES}"

algorithm_names = {
    1: "A*",
    2: "Uniform-cost",
    3: "Greedy search"
}

heuristic_names = {
    1: "Manhattan-distance",
    2: "Linear conflict",
    3: "Misplaced tiles"
}

def handle_sigint(signum, frame):
    print("\nBye bye!")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def a_star(heuristic, field, goal, flat_goal, size):

    """ heuristic - int index, 
    field - initial state as a tuple, 
    goal - dictionary with the target state and coordinates for each tile,
    flat_goal - tuple representation of the goal,
    size - the lenght of a side of the field in int """

    # CHECK IF SOLVABLE
    # print("goal :", flat_goal)
    # INITIATING
    opened = []     # Opened states - prioritized queue
    closed = set()  # Closed states
    came_from = {}  # Parents map: came_from[current] = parent
    max_nodes = 1   # Maximum nodes in memory
    total_opened = 0 # Total opened states
    g_scores = {field: 0} # Memorizing g for each state to avoid recounting
    # the queue, f, g, state, previous state
    heapq.heappush(opened, (heuristics[heuristic](field, goal, size), 0, field, None))

    while opened:
        total_opened += 1
        # print(f"LOOP START, total opened: {total_opened}, opened set: {opened}")
        f, g, cur, parent = heapq.heappop(opened)

        if cur in closed:
            continue

        came_from[cur] = parent
        closed.add(cur)

        if cur == flat_goal:
            print_output(find_path(came_from, cur), total_opened, max_nodes, size)
            return

        for neighbor in get_neighbors(cur, size):
            if neighbor in closed:
                continue
            new_g = g + 1
            if neighbor not in g_scores or new_g < g_scores[neighbor]:
                g_scores[neighbor] = new_g
                new_f = new_g + heuristics[heuristic](neighbor, goal, size)
                heapq.heappush(opened, (new_f, new_g, neighbor, cur))
            
        max_nodes = max(max_nodes, len(opened) + len(closed))

    # neighbors = get_neighbors(field, size)
    # print(neighbors)
    # dist = heuristics[heuristic](field, goal, size)

    print(f"Sorry, no solution found")

def print_output(path, total_opened, max_nodes, size):
    print(f"\n✅ {GREEN}Solved in {BOLD}{len(path) - 1} moves{RES}")
    print(f"🧠 {GREEN}Time complexity: {BOLD}{total_opened}{RES}")
    print(f"💾 {GREEN}Space complexity: {BOLD}{max_nodes}{RES}{RES}")
    print(f"🧩 {GREEN}Solution path:\n{RES}")
    i = 0
    for state in path:
        print(f"{YELLOW}Step {i}:{RES}")
        print_field(state, size)
        i += 1
    
    save_to_file(path, total_opened, max_nodes, size)
    return

def save_to_file(path, total_opened, max_nodes, size):
    
    with open("solution.txt", "w") as f:

        f.write(f"✅ {GREEN}Solved in {BOLD}{len(path) - 1} moves{RES}\n")
        f.write(f"🧠 {GREEN}Time complexity: {BOLD}{total_opened}{RES}\n")
        f.write(f"💾 {GREEN}Space complexity: {BOLD}{max_nodes}{RES}\n")
        f.write(f"🧩 {GREEN}Solution path:\n{RES}")
        for step, state in enumerate(path):
            f.write(f"\n{YELLOW}Step {step}:{RES}\n")
            for i in range(size):
                row = " ".join(f"{state[i * size + j]:2}" for j in range(size))
                f.write(row + "\n")
    print(f"✅ Solution path saved to 'solution.txt'")
            

def find_path(came_from, cur):
    path = []
    while cur:
        path.append(cur)
        cur = came_from[cur]
    return path[::-1]

def manhattan_distance(state, goal, size):
    dist = 0
    for index, val in enumerate(state):
        if val == 0:
            continue
        row, col = divmod(index, size)
        goal_row, goal_col = goal[val]
        dist += abs(goal_row - row) + abs(goal_col - col)
    return dist



algorithms = {
    1: a_star
}

heuristics = {
    1: manhattan_distance
    # 2: linear_conflict
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


def print_field(field, size):
    for i in range(0, len(field), size):
        row = field[i:i+size]
        print(" ".join(str(cell) for cell in row))
    print("\n")

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
    # print(goal)
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
                if size < MINP or size > MAXP:
                    raise ValueError(f"Board size must be between {MINP} and {MAXP}") 
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
    

def generate_field(size):

    field = tuple(random.sample(range(0, size * size), size * size))
    return field

def choose_number(msg, minval, maxval):
    try:
        user_size = input(msg)
        size = int(user_size)
        if minval <= size <= maxval:
            return size
        else:
            raise ValueError
    except ValueError:
        print(f"{RED}Error: invalid value. Introduce value between {minval} and {maxval} {RES}\n")
        return choose_number(msg, minval, maxval)

def main(args):

    if len(args) == 1:
        size = choose_number(MSG_PZL_SIZE, MINP, MAXP)
        field = generate_field(size) # IT SHOULD BE MAYBE AN OBJECT (CLASS)???
    elif len(args) == 2:
        try:
            size, field = parse_field(args[1])
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print(f"{RED}Too many arguments")
        sys.exit(1)
    
    map_goal, flat_goal = create_goal_positions(generate_goal(size))
    
    # print(flat_goal)
    print(f"\nYour field size is: {size}\n\nYour field is:")
    print_field(field, size)
    heuristic = 0

    try:
        algo = choose_number(MSG_ALGO, 1, 3)
        if algo == 1: 
            heuristic = choose_number(MSG_HEURISTIC, 1, 3)
        print(f"\n{BLUE}Chosen algorithm: {algorithm_names[algo]}, chosen heristic: {heuristic_names[heuristic]}{RES}")
    except EOFError:
        print("\nBye bye!")
        sys.exit(0)

    algorithms[algo](heuristic, field, map_goal, flat_goal, size)
    # THE ALGORITHM HERE  
    

if __name__ == "__main__":
    main(sys.argv)