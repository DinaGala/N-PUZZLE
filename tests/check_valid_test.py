import unittest
from solver.checker import is_solvable_matrix, is_solvable

class TestPuzzleSolvable(unittest.TestCase):
    # --- Matrix-based tests ---
    def test_solvable_3x3(self):
        puzzle = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        self.assertTrue(is_solvable_matrix(puzzle))

    def test_unsolvable_3x3(self):
        puzzle = [
            [1, 2, 3],
            [4, 5, 6],
            [8, 7, 0]
        ]
        self.assertFalse(is_solvable_matrix(puzzle))

    def test_solvable_4x4(self):
        puzzle = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 15, 14, 0]
        ]
        self.assertTrue(is_solvable_matrix(puzzle))

    def test_unsolvable_4x4(self):
        puzzle = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [15, 13, 14, 0]
        ]
        self.assertFalse(is_solvable_matrix(puzzle))

    # --- Flattened input tests ---
    def test_solvable_flatten_3x3(self):
        flatten = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertTrue(is_solvable(flatten, 3))

    def test_unsolvable_flatten_3x3(self):
        flatten = [1, 2, 3, 4, 5, 6, 8, 7, 0]
        self.assertFalse(is_solvable(flatten, 3))

    def test_solvable_flatten_4x4(self):
        flatten = [1, 2, 3, 4,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   13, 15, 14, 0]
        self.assertTrue(is_solvable(flatten, 4))

    def test_unsolvable_flatten_4x4(self):
        flatten = [1, 2, 3, 4,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   15, 13, 14, 0]
        self.assertFalse(is_solvable(flatten, 4))


if __name__ == '__main__':
    unittest.main()
