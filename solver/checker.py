from typing import List, Tuple

def count_inversion(arr: List[int]) -> int:
    """
    Count the number of inversions : An inversion is a pair of indices (i, j) 
    such that i < j and arr[i] > arr[j]. This represents a disorder in the sequence.
    1. Initialize the inversion counter
    2. Iterate over all pairs (i, j) with i < j
    3. An inversion occurs when an earlier element is greater than a later one
    """
    count_inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count_inv += 1
    return count_inv

def solvable_odd(arr:List[int], arr_goal:List[int])->bool:
    '''
    if puzzle size is odd : solvable if inversion parity is the same between start and goal state"

    '''
    nb_inv_goal = count_inversion(arr_goal)
    nb_inv = count_inversion(arr)
        
    return (nb_inv % 2) == (nb_inv_goal % 2)

def solvable_even(arr:List[int], arr_goal:List[int], bottom_pos : int, bottom_goal : int)-> bool:
    '''
    solvable if (inversions + blank_row_from_bottom) is same parity for raw vs goal state
    '''
    nb_inv = count_inversion(arr)
    nb_inv_goal = count_inversion(arr_goal)    
    
    nb_inv += bottom_pos
    nb_inv_goal += bottom_goal

    return (nb_inv % 2) == (nb_inv_goal % 2) 


def is_solvable(flatten_full: List[int], goal_raw : List[int], size : int)->bool:
    '''
    Every legal move in the N-puzzle (swapping the blank with a neighbor) corresponds 
    to a transposition of adjacent elements in the flattened version. That means solving the puzzle is equivalent 
    to performing a series of legal adjacent swaps to sort the list into the goal configuration.
    From a mathematical point of view, the set of all permutations of a list can be divided into:
    Even permutations: which can be reached by an even number of swaps
    Odd permutations: which require an odd number of swaps
    '''
    #extract the 0 row idx
    blank_pos = -1
    blank_goal_pos = -1
    
    for i in range(len(flatten_full)):
        if flatten_full[i] == 0:
            blank_pos = size - (i // size)
            break
    for i in range(len(goal_raw)):
        if goal_raw[i] == 0:
            blank_goal_pos = size - i // size
            break
    
    #take all values but zero to look for inversion
    flatten = [x for x in flatten_full if x != 0]
    goal_state = [x for x in goal_raw if x != 0]
    if blank_pos == -1 or blank_goal_pos == -1:
        return False
    #if even Puzzle
    if (size % 2 == 0):
        return solvable_even(flatten, goal_state, blank_pos, blank_goal_pos)
    return solvable_odd(flatten, goal_state)

