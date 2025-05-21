# script.py
import sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RES = "\033[0m"
BOLD = "\033[1m"
MINP = 3
MAXP = 9
MSG_PZL_SIZE = "{GREEN}Choose the size of the puzzle (from {MIN} to {MAX}):  {RES}"

# sys.argv[0] is the script name
# sys.argv[1], [2], ... are the actual arguments

def parse_field(filename):
    print(filename)
    # parse the firld here
    mytupplefield = (
        1, 2, 3, 
        4, 5, 6,
        7, 8, 0
        )
    return mytupplefield

def generate_field(size):
    # here is the field generator
    mytupplefield = (
        1, 2, 3, 
        4, 5, 6,
        7, 8, 0
        )
    return mytupplefield

def choose_number(msg):
    try:
        user_size = input(f"{GREEN}Choose the size of the puzzle (from {MIN} to {MAX}):  {RES}")
        size = int(user_size)
        if MIN <= size <= MAX:
            return size
        else:
            raise ValueError
    except ValueError:
        print(f"{RED}Please enter a value between {MIN} and {MAX} !!!{RES}")
        return choose_number()

def main(args):
    if len(args) == 1:
        size = choose_number("{GREEN}Choose the size of the puzzle (from {MIN} to {MAX}):  {RES}")
        field = generate_field(size) # IT SHOULD BE MAYBE AN OBJECT (CLASS)???
    elif len(args) == 2:
        field = parse_field(args[1])
    else:
        print(f"{RED}Too many arguments")
        sys.exit(1)

    try:
        number = input(f"{BLUE}1. A*\n2.Uniform-cost\n3.Greedy search\nChoose the algorithm: ")

        
    print(size)
    # sys.exit(1)

# name = sys.argv[1]
# print(f"Hello, {name}!")

if __name__ == "__main__":
    main(sys.argv)