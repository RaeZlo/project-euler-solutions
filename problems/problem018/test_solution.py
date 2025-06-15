import unittest
from solution import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_small_triangle(self):
        triangle = [
            [3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]
        ]
        self.assertEqual(max_path_sum(triangle), 23)

    def test_single_element(self):
        triangle = [[5]]
        self.assertEqual(max_path_sum(triangle), 5)

    def test_two_rows(self):
        triangle = [
            [1],
            [2, 3]
        ]
        self.assertEqual(max_path_sum(triangle), 4)

    def test_large_triangle(self):
        triangle = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
        ]
        self.assertEqual(max_path_sum(triangle), 1074)

    def test_flat_triangle(self):
        triangle = [
            [1],
            [1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(max_path_sum(triangle), 3)

    def test_empty_triangle(self):
        triangle = []
        self.assertEqual(max_path_sum(triangle), 0)

    def test_negative_numbers(self):
        triangle = [
            [-1],
            [-2, -3],
            [-4, -5, -6]
        ]
        self.assertEqual(max_path_sum(triangle), -7)  # -1 + -2 + -4

    def test_mixed_numbers(self):
        triangle = [
            [2],
            [3, 4],
            [6, -5, 7],
            [4, 1, 8, 3]
        ]
        self.assertEqual(max_path_sum(triangle), 21)  # 2 + 4 + 7 + 8

    def test_multiple_max_paths(self):
        triangle = [
            [5],
            [1, 1],
            [1, 9, 1],
            [9, 1, 1, 9]
        ]
        self.assertEqual(max_path_sum(triangle), 16)

if __name__ == '__main__':
    unittest.main()
