from .macros import RED, GREEN, YELLOW, BLUE, RES, BOLD

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

def print_field(field, size):

    for i in range(0, len(field), size):
        row = field[i:i+size]
        print(" ".join(str(cell) for cell in row))
    print("\n")

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