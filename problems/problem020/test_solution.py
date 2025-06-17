import unittest
from solution import factorial_digit_sum

class TestFactorialDigitSum(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(factorial_digit_sum(1), 1)     # 1! = 1 → 1
        self.assertEqual(factorial_digit_sum(2), 2)     # 2! = 2 → 2
        self.assertEqual(factorial_digit_sum(5), 3)     # 5! = 120 → 1+2+0 = 3

    def test_known_values(self):
        self.assertEqual(factorial_digit_sum(10), 27)   # 10! = 3628800 → sum = 27
        self.assertEqual(factorial_digit_sum(100), 648) # Resultado conocido del problema

    def test_zero(self):
        self.assertEqual(factorial_digit_sum(0), 1)     # 0! = 1 → 1

    def test_medium_range(self):
        self.assertEqual(factorial_digit_sum(20), sum(int(d) for d in str(2432902008176640000)))
        self.assertEqual(factorial_digit_sum(25), sum(int(d) for d in str(15511210043330985984000000)))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            factorial_digit_sum("10")  # string en lugar de int

        with self.assertRaises(TypeError):
            factorial_digit_sum(None)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial_digit_sum(-5)

if __name__ == "__main__":
    unittest.main()
