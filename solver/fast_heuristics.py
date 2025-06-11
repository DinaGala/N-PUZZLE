# solver/fast_heuristics.py
from .c_heuristics import manhattan_distance, linear_conflict, misplaced_tiles, no_heuristic

heuristics = {
    0: no_heuristic,
    1: manhattan_distance,
    2: linear_conflict,
    3: misplaced_tiles,
}