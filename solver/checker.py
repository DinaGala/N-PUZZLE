from typing import List, Tuple

def flatten_matrix(mtrx:List[List[int]])->Tuple[List[int], int]: 
    flatten = [val for row in mtrx for val in row if val != 0]
    blank_row_from_bottom = -1
    
    for row_idx in range(len(mtrx)):
        if 0 in mtrx[row_idx]:
            blank_row_from_bottom = len(mtrx) - row_idx
            break # stop at the first (and only) blank
    return (flatten, blank_row_from_bottom) 


def is_even_size(mtrx:List[List[int]])->bool:
    return len(mtrx) % 2 == 0

def count_inversion(arr: List[int]) -> int:
    count_inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count_inv += 1
    return count_inv

def solvable_odd(arr:List[int])->bool:
    '''
    if puzzle size is odd -> solvable if number of invesion is even
    '''
    return (count_inversion(arr)) % 2 == 0 

def solvable_even(arr:List[int], bottom_pos : int)-> bool:
    '''
    solvable if (inversions + blank_row_from_bottom) is even
    '''
    nb_inv = count_inversion(arr)
    return (nb_inv + bottom_pos) % 2 == 0 

def is_solvable_matrix(mtrx: List[List[int]])->bool:
    '''
    Every legal move in the N-puzzle (swapping the blank with a neighbor) corresponds to a transposition of adjacent elements in the flattened version. That means solving the puzzle is equivalent to performing a series of legal adjacent swaps to sort the list into the goal configuration.
    From a mathematical point of view, the set of all permutations of a list can be divided into:
    Even permutations: which can be reached by an even number of swaps
    Odd permutations: which require an odd number of swaps
    '''
    flatten, blank_pos = flatten_matrix(mtrx)
    if blank_pos == -1:
        return False
    if (is_even_size(mtrx)):
        return solvable_even(flatten, blank_pos)
    return solvable_odd(flatten)

def is_solvable(flatten_full: List[int], size : int)->bool:
    '''
    Every legal move in the N-puzzle (swapping the blank with a neighbor) corresponds to a transposition of adjacent elements in the flattened version. That means solving the puzzle is equivalent to performing a series of legal adjacent swaps to sort the list into the goal configuration.
    From a mathematical point of view, the set of all permutations of a list can be divided into:
    Even permutations: which can be reached by an even number of swaps
    Odd permutations: which require an odd number of swaps
    '''
    #take all values but zero
    blank_pos = -1
    for i in range(len(flatten_full)):
        if flatten[i] == 0:
            blank_pos = size - (i // size)
            break
    from typing import List, Tuple

def flatten_matrix(mtrx:List[List[int]])->Tuple[List[int], int]: 
    flatten = [val for row in mtrx for val in row if val != 0]
    blank_row_from_bottom = -1
    
    for row_idx in range(len(mtrx)):
        if 0 in mtrx[row_idx]:
            blank_row_from_bottom = len(mtrx) - row_idx
            break # stop at the first (and only) blank
    return (flatten, blank_row_from_bottom) 


def is_even_size(mtrx:List[List[int]])->bool:
    return len(mtrx) % 2 == 0

def count_inversion(arr: List[int]) -> int:
    count_inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count_inv += 1
    return count_inv

def solvable_odd(arr:List[int])->bool:
    '''
    if puzzle size is odd -> solvable if number of invesion is even
    '''
    return (count_inversion(arr)) % 2 == 0 

def solvable_even(arr:List[int], bottom_pos : int)-> bool:
    '''
    solvable if (inversions + blank_row_from_bottom) is even
    '''
    nb_inv = count_inversion(arr)
    return (nb_inv + bottom_pos) % 2 == 0 

def is_solvable_matrix(mtrx: List[List[int]])->bool:
    '''
    Every legal move in the N-puzzle (swapping the blank with a neighbor) corresponds to a transposition of adjacent elements in the flattened version. That means solving the puzzle is equivalent to performing a series of legal adjacent swaps to sort the list into the goal configuration.
    From a mathematical point of view, the set of all permutations of a list can be divided into:
    Even permutations: which can be reached by an even number of swaps
    Odd permutations: which require an odd number of swaps
    '''
    flatten, blank_pos = flatten_matrix(mtrx)
    if blank_pos == -1:
        return False
    if (is_even_size(mtrx)):
        return solvable_even(flatten, blank_pos)
    return solvable_odd(flatten)

def is_solvable(flatten_full: List[int], size : int)->bool:
    '''
    Every legal move in the N-puzzle (swapping the blank with a neighbor) corresponds to a transposition of adjacent elements in the flattened version. That means solving the puzzle is equivalent to performing a series of legal adjacent swaps to sort the list into the goal configuration.
    From a mathematical point of view, the set of all permutations of a list can be divided into:
    Even permutations: which can be reached by an even number of swaps
    Odd permutations: which require an odd number of swaps
    '''
    #extract the 0 row idx
    blank_pos = -1
    for i in range(len(flatten_full)):
        if flatten_full[i] == 0:
            blank_pos = size - (i // size)
            break
    #take all values but zero to look for inversion
    flatten = [x for x in flatten_full if x != 0]
    if blank_pos == -1:
        return False
    #if even Puzzle
    if (size % 2 == 0):
        return solvable_even(flatten, blank_pos)
    return solvable_odd(flatten)

