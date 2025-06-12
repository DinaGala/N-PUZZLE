from .macros import RED, GREEN, YELLOW, BLUE, RES, BOLD
import datetime, os

def print_output(path, total_opened, max_nodes, size, time):
    print(f"\n✅ {GREEN}Solved in {BOLD}{len(path) - 1} moves{RES}")
    print(f"🧠 {GREEN}Time complexity: {BOLD}{total_opened}{RES}")
    print(f"💾 {GREEN}Space complexity: {BOLD}{max_nodes}{RES}")
    print(f"💾 {GREEN}Total compute time (sec): {BOLD}{time:.4f}{RES}")
    print(f"🧩 {GREEN}Solution path:\n{RES}")
    # i = 0
    # for state in path:
    #     print(f"{YELLOW}Step {i}:{RES}")
    #     print_field(state, size)
    #     i += 1
    
    save_to_file(path, total_opened, max_nodes, size, time)
    return

def print_field(field, size):

    for i in range(0, len(field), size):
        row = field[i:i+size]
        print(" ".join(str(cell) for cell in row))
    print("\n")

def save_to_file(path, total_opened, max_nodes, size, time):
    
    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    os.makedirs("solutions", exist_ok=True)
    file = "solutions/solution_" + dt + ".txt"

    with open(file, "w") as f:

        f.write(f"✅ Solved in {len(path) - 1} moves\n")
        f.write(f"🧠 Time complexity: {total_opened}\n")
        f.write(f"💾 Space complexity: {max_nodes}\n")
        f.write(f"💾 Total compute time (sec): {time:.4f}\n")
        f.write(f"🧩 Solution path:\n")
        for step, state in enumerate(path):
            f.write(f"\nStep {step}:\n")
            for i in range(size):
                row = " ".join(f"{state[i * size + j]:2}" for j in range(size))
                f.write(row + "\n")
    print(f"✅ Solution path saved to {file}")
            

def find_path(came_from, cur):
    path = []
    while cur:
        path.append(cur)
        cur = came_from[cur]
    return path[::-1]