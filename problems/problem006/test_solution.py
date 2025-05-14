import unittest
from solution import sum_square_difference

class TestSumSquareDifference(unittest.TestCase):

    def test_example_case(self):
        # Caso del enunciado: n = 10
        # (1 + 2 + ... + 10)^2 = 3025
        # 1^2 + 2^2 + ... + 10^2 = 385
        # 3025 - 385 = 2640
        self.assertEqual(sum_square_difference(10), 2640)

    def test_small_cases(self):
        self.assertEqual(sum_square_difference(1), 0)   # 1^2 - 1^2 = 0
        self.assertEqual(sum_square_difference(2), 4)   # (1+2)^2 - (1^2 + 2^2) = 9 - 5 = 4
        self.assertEqual(sum_square_difference(3), 22)  # 36 - 14

    def test_large_case(self):
        self.assertEqual(sum_square_difference(100), 25164150)

if __name__ == "__main__":
    unittest.main()
