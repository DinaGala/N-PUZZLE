# script.py
import sys
import random

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

algorithms = {
    1: "A*",
    2: "Uniform-cost",
    3: "Greedy search"
}

heuristics = {
    1: "Manhattan-distance",
    2: "Euclidian distance",
    3: "..."
}

# sys.argv[0] is the script name
# sys.argv[1], [2], ... are the actual arguments

def print_field(field, size):
    for i in range(0, len(field), size):
        row = field[i:i+size]
        print(" ".join(str(cell) for cell in row))

def parse_field(filename):
    print(filename)
    # parse the firld here
    # field = []
    size = 3
    
    mytupplefield = (
        1, 2, 3, 
        4, 5, 6,
        7, 8, 0
        )
    return size, mytupplefield

def generate_field(size):
    # here is the field generator
    # print(size)
    mytupplefield = tuple(random.sample(range(0, size * size), size * size))

    # mytupplefield = (
    #     1, 2, 3, 
    #     4, 5, 6,
    #     7, 8, 0
    #     )
    return mytupplefield

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
        print_field(field, size)
    elif len(args) == 2:
        size, field = parse_field(args[1])
    else:
        print(f"{RED}Too many arguments")
        sys.exit(1)

    algo = choose_number(MSG_ALGO, 1, 3)
    heuristic = choose_number(MSG_HEURISTIC, 1, 3)

        
    print(f"\n{BLUE}Chosen algorithm: {algorithms[algo]}, chosen heristic: {heuristics[heuristic]}{RES}")
    # sys.exit(1)

# name = sys.argv[1]
# print(f"Hello, {name}!")

if __name__ == "__main__":
    main(sys.argv)