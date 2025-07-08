import unittest
from solution import number_spiral_diagonals

class TestNumberSpiralDiagonals(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(number_spiral_diagonals(1), 1)

    def test_small_spiral(self):
        self.assertEqual(number_spiral_diagonals(3), 25)

    def test_medium_spiral(self):
        self.assertEqual(number_spiral_diagonals(5), 101)

    def test_large_spiral(self):
        self.assertEqual(number_spiral_diagonals(1001), 669171001)

    def test_invalid_even_input(self):
        with self.assertRaises(ValueError):
            number_spiral_diagonals(4)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            number_spiral_diagonals(-3)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            number_spiral_diagonals(0)

if __name__ == '__main__':
    unittest.main()
