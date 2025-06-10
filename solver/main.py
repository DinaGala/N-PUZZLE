import sys
import signal
from .parser import generate_field, parse_field, create_goal_positions, generate_goal
from .a_star import algorithms
from .checker import is_solvable
from .output import print_field
from .macros import RED, GREEN, YELLOW, BLUE, RES, MINP, MAXP, MSG_ALGO, MSG_HEURISTIC, MSG_PZL_SIZE, algorithm_names, heuristic_names

def main(args):

    if len(args) == 1:
        size = choose_number(MSG_PZL_SIZE, MINP, MAXP)
        field = generate_field(size) 
    elif len(args) == 2:
        try:
            size, field = parse_field(args[1])
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print(f"{RED}Too many arguments")
        sys.exit(1)
    
    goal, goal_state = create_goal_positions(generate_goal(size))

    print(f"\nYour field size is: {size}\n\nYour field is:")
    print_field(field, size)
    print(f"\nYour goal state is:")
    print_field(goal_state, size)
    heuristic = 0

    # print(goal[2])

    try:
        algo = choose_number(MSG_ALGO, 1, 3)
        # if algo == 1: 
        heuristic = choose_number(MSG_HEURISTIC, 1, 3)
        print(f"\n{BLUE}Chosen algorithm: {algorithm_names[algo]}, chosen heristic: {heuristic_names[heuristic]}{RES}")
    except EOFError:
        print("\nBye bye!")
        sys.exit(0)
    
    if not is_solvable(field, goal_state, size):
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

def handle_sigint(signum, frame):
    print("\nBye bye!")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

if __name__ == "__main__":
    main(sys.argv)