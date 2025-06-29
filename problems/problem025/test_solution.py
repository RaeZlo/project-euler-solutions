import unittest
from solution import find_fibonacci_index_with_digits

class TestFibonacciIndexWithDigits(unittest.TestCase):

    def test_single_digit(self):
        # F1 = 1, F2 = 1 → el primero con 1 dígito es F1
        self.assertEqual(find_fibonacci_index_with_digits(1), 1)

    def test_two_digits(self):
        # F7 = 13 tiene 2 dígitos
        self.assertEqual(find_fibonacci_index_with_digits(2), 7)

    def test_three_digits(self):
        # F12 = 144 tiene 3 dígitos
        self.assertEqual(find_fibonacci_index_with_digits(3), 12)

    def test_large_digits(self):
        # Caso principal del problema de Project Euler
        self.assertEqual(find_fibonacci_index_with_digits(1000), 4782)

    def test_medium_digits(self):
        # F239 tiene 500 dígitos
        self.assertEqual(find_fibonacci_index_with_digits(500), 2390)

    def test_zero_digits(self):
        # Decidimos que para n <= 1, el resultado es 1
        self.assertEqual(find_fibonacci_index_with_digits(0), 1)

    def test_negative_digits(self):
        self.assertEqual(find_fibonacci_index_with_digits(-10), 1)

if __name__ == "__main__":
    unittest.main()
