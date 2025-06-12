RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RES = "\033[0m"
BOLD = "\033[1m"
MINP = 2
MAXP = 9

algorithm_names = {
    1: "A*",
    2: "Uniform-cost",
    3: "Greedy search"
}

heuristic_names = {
    0: "No heuristic",
    1: "Manhattan-distance",
    2: "Linear conflict",
    3: "Misplaced tiles"
}

MSG_PZL_SIZE = f"{GREEN}Choose the size of the puzzle (from {MINP} to {MAXP}):  {RES}"
MSG_ALGO = f"{BLUE}1. {algorithm_names[1]}\n2.{algorithm_names[2]}\n3.{algorithm_names[3]}{RES}\n{GREEN}Choose the algorithm:  {RES}"
MSG_HEURISTIC = f"{BLUE}1. {heuristic_names[1]}\n2. {heuristic_names[2]}\n3. {heuristic_names[3]}{RES}\n{GREEN}Choose the heuristic:  {RES}"
