import unittest
from solution import is_digit_cancelling, solve

class TestDigitCancellingFractions(unittest.TestCase):

    def test_valid_fractions(self):
        self.assertTrue(is_digit_cancelling(49, 98))
        self.assertTrue(is_digit_cancelling(26, 65))
        self.assertTrue(is_digit_cancelling(19, 95))
        self.assertTrue(is_digit_cancelling(16, 64))

    def test_invalid_fractions(self):
        self.assertFalse(is_digit_cancelling(30, 50))  # Trivial
        self.assertFalse(is_digit_cancelling(11, 22))  # Trivial
        self.assertFalse(is_digit_cancelling(21, 31))  # No cumple condición
        self.assertFalse(is_digit_cancelling(12, 34))  # No cumple condición
        self.assertFalse(is_digit_cancelling(40, 80))  # Trivial

    def test_final_solution(self):
        self.assertEqual(solve(), 100)

if __name__ == "__main__":
    unittest.main()
