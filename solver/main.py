import sys
import signal
from .parser import generate_field, parse_field, create_goal_positions, generate_goal
from .a_star import algorithms
from .checker import is_solvable

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RES = "\033[0m"
BOLD = "\033[1m"
MINP = 3
MAXP = 9
MSG_PZL_SIZE = f"{GREEN}Choose the size of the puzzle (from {MINP} to {MAXP}):  {RES}"
MSG_ALGO = f"{BLUE}1. A*\n2.Uniform-cost\n3.Greedy search{RES}\n{GREEN}Choose the algorithm:  {RES}"
MSG_HEURISTIC = f"{BLUE}1. Manhattan-distance\n2. Euclidian distance\n3. ...{RES}\n{GREEN}Choose the heuristic:  {RES}"

algorithm_names = {
    1: "A*",
    2: "Uniform-cost",
    3: "Greedy search"
}

heuristic_names = {
    1: "Manhattan-distance",
    2: "Misplaced tiles",
    3: "Linear conflict"
}

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
    
    goal_matrix = generate_goal(size)
    goal_state = tuple(val for row in goal_matrix for val in row)
    goal = create_goal_positions(goal_matrix)
    print(goal)
    print_field(field, size)

    try:
        algo = choose_number(MSG_ALGO, 1, 3)
        heuristic = choose_number(MSG_HEURISTIC, 1, 3)
        print(f"\n{BLUE}Chosen algorithm: {algorithm_names[algo]}, chosen heristic: {heuristic_names[heuristic]}{RES}")
    except EOFError:
        print("\nBye bye!")
        sys.exit(0)
    
    if not is_solvable(field, size):
        print(f"\n{RED}Puzzle Impossible to solve{RES}\n")
        sys.exit(0)
    print(f"\n{GREEN}Puzzle Solvable{RES}\n")
    
    algorithms[algo](heuristic, field, goal, goal_state, size)
    
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

def print_field(field, size):

    print(f"\nYour field size is: {size}\n\nYour field is:")
    for i in range(0, len(field), size):
        row = field[i:i+size]
        print(" ".join(str(cell) for cell in row))
    print("\n")

def handle_sigint(signum, frame):
    print("\nBye bye!")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

if __name__ == "__main__":
    main(sys.argv)