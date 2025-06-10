import unittest
from solver.checker import is_solvable, count_inversion
from solver.main import create_goal_positions, generate_goal

class TestPuzzleSolvable(unittest.TestCase):

    # --- Flattened input tests ---
    """
    3x3 test goal snail is :
   
        1  2  3  
        8  0  4
        4  6  5
 
    has 7 inversions -> odd N szie so should be valid for an odd nb of inversion only
    """
    def test_solvable_snail_3x3(self):
        # Dina's matrix -> Same parity as snail goal (odd → odd)
        flatten = [3, 2, 6, 1, 4, 0, 8, 7, 5]  # 9 inversions → odd
        size = 3
        _, goal = create_goal_positions(generate_goal(size))
        self.assertTrue(is_solvable(flatten, goal, size))

    def test_unsolvable_snail_3x3(self):
        # Different parity from snail goal (even ≠ odd)
        flatten = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # 0 inversions → even
        size = 3
        _, goal = create_goal_positions(generate_goal(size))
        self.assertFalse(is_solvable(flatten, goal, size))

    def test_unsolvable_snail_3x3_edge_case(self):
        flatten = [1, 2, 3, 8, 4, 0, 7, 5, 6]  # 6 inversions → even
        size = 3
        _, goal = create_goal_positions(generate_goal(size))
        self.assertFalse(is_solvable(flatten, goal, size))

    def test_solvable_snail_3x3_edge_case(self):
        flatten = [1, 2, 3, 8, 4, 0, 6, 5, 7]  # 5 inversions → even
        size = 3
        _, goal = create_goal_positions(generate_goal(size))
        self.assertTrue(is_solvable(flatten, goal, size))
    
    """
    Test on 4x4, goal state is 
    
        1   2   3   4
        12  13  14   5
        11   0  15   6
        10   9   8   7
    
    that's 37 inversions -> we compare parity between 
    the nb inversion and bottom position in goal vs init state
    for snail goal, bottom position for blank is 2 (1 row above bottom at value initial 1 for bottom)
    so total is 39 % 2 -> odd parity for goal state
    """
    def test_solvable_snail_4x4(self):
        #41 inversion -> bottom at position 2 -> 43 % 2 = 1 -> possible 
        flatten = [
            1, 2, 3, 4,
            12, 13, 14, 5,
            11, 0, 15, 6,
            10, 9, 8, 7
        ]
        size = 4
        _, goal = create_goal_positions(generate_goal(size))
        self.assertTrue(is_solvable(flatten, goal, size))  # same as goal, 41 inversions

    def test_solvable_snail_4x4(self):
        flatten = [
            1, 2, 3, 4,
            12, 13, 14, 5,
            11, 15, 0, 6,
            10, 9, 8, 7
        ]

        size = 4
        _, goal = create_goal_positions(generate_goal(size))
        self.assertTrue(is_solvable(flatten, goal, size))
    
    def test_odd_4x4(self):
        #odd nbr of inversio -> ok check
        odd = [
            1, 2, 3, 4, 12, 13, 14, 
            5,11, 0, 15, 6,10, 9, 8, 7
        ]

        size = 4
        _, goal = create_goal_positions(generate_goal(size))
        self.assertTrue(is_solvable(odd, goal, size))
    
    def test_even_4x4(self):
        # even so impossible
        even = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 15, 0, 6],
            [10, 9, 8, 7]
        ]
        size = 4
        _, goal = create_goal_positions(generate_goal(size))
        self.assertFalse(is_solvable(even, goal, size))
    
    def test_from_subject(self):
        #should be impossible : nb of inversion is 48 -> blank at pos 4 -> 52 (even)
        size = 4
        flatten_ponies = [
            0, 10,  5,  7,
            11, 14,  4,  8,
            1,  2,  6, 13,
            12,  3, 15,  9
        ]
        _, goal = create_goal_positions(generate_goal(size))
        self.assertFalse(is_solvable(flatten_ponies, goal, size))

    """
    Test on 5x5, goal state is 
    
        1   2   3   4   5
        16  17  18  19   6
        15  24   0  20   7
        14  23  22  21   8
        13  12  11  10   9
    
    that's 105 inversions -> we compare parity directly in inv nbr so 
    nb of inversion in raw state needs to be odd
    """
    def test_solvability_5x5_cases(self):
        size = 5
        _, goal = create_goal_positions(generate_goal(size))  # flattened snail goal

        # Test 1 – Solvable: blank moved right
        flatten1 = [
            1, 2, 3, 4, 5,
            16, 17, 18, 19, 6,
            15, 24, 20, 0, 7,
            14, 23, 22, 21, 8,
            13, 12, 11, 10, 9
        ]
        self.assertTrue(is_solvable(flatten1, goal, size))

        #Test 2 – Unsolvable: 9 and 10 swapped
        flatten2 = [
            1, 2, 3, 4, 5,
            16, 17, 18, 19, 6,
            15, 24, 0, 20, 7,
            14, 23, 22, 21, 8,
            13, 12, 11, 9, 10  # 9 and 10 swapped
        ]
        self.assertFalse(is_solvable(flatten2, goal, size))

        # Test 3 – Unsolvable: mirrored blocks -> 30 inversions (even)
        flatten3 = [
            5, 4, 3, 2, 1,
            6, 7, 8, 9, 10,
            15, 14, 13, 12, 11,
            16, 17, 18, 19, 0,
            24, 23, 22, 21, 20
        ]
        self.assertFalse(is_solvable(flatten3, goal, size))

        # Test 4 – Unsolvable: row-major solved state
        flatten4 = [
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15,
            16, 17, 18, 19, 20,
            21, 22, 23, 24, 0
        ]
        self.assertFalse(is_solvable(flatten4, goal, size))


if __name__ == '__main__':
    unittest.main()
