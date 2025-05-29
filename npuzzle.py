# script.py
import sys
import random
import signal

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
    2: "Misplaced tiles",
    3: "Linear conflict"
}

def handle_sigint(signum, frame):
    print("\nBye bye!")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

# sys.argv[0] is the script name
# sys.argv[1], [2], ... are the actual arguments

def print_field(field, size):

    print(f"\nYour field size is: {size}\n\nYour field is:")
    for i in range(0, len(field), size):
        row = field[i:i+size]
        print(" ".join(str(cell) for cell in row))

    print("\n")

def parse_field(filename):
    # print(filename)

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

            # if size is None:
            #     raise ValueError("Board size is not specified.")

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

    return size, tuple(field)
    
    # mytupplefield = (
    #     1, 2, 3, 
    #     4, 5, 6,
    #     7, 8, 0
    #     )
    # return size, mytupplefield

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
    elif len(args) == 2:
        try:
            size, field = parse_field(args[1])
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print(f"{RED}Too many arguments")
        sys.exit(1)
    
    print_field(field, size)

    try:
        algo = choose_number(MSG_ALGO, 1, 3)
        heuristic = choose_number(MSG_HEURISTIC, 1, 3)
        print(f"\n{BLUE}Chosen algorithm: {algorithms[algo]}, chosen heristic: {heuristics[heuristic]}{RES}")
    except EOFError:
        print("\nBye bye!")
        sys.exit(0)

        
    
    # sys.exit(1)



if __name__ == "__main__":
    main(sys.argv)