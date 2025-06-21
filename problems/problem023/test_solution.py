import unittest
from solution import (
    sum_of_proper_divisors,
    is_abundant,
    solve,
)

class TestProblem023(unittest.TestCase):

    def test_sum_of_proper_divisors(self):
        # Casos base
        self.assertEqual(sum_of_proper_divisors(1), 0)
        self.assertEqual(sum_of_proper_divisors(2), 1)
        self.assertEqual(sum_of_proper_divisors(3), 1)
        self.assertEqual(sum_of_proper_divisors(6), 1 + 2 + 3)  # Perfect number
        self.assertEqual(sum_of_proper_divisors(12), 1 + 2 + 3 + 4 + 6)

    def test_is_abundant(self):
        self.assertFalse(is_abundant(28))  # Perfect number
        self.assertTrue(is_abundant(12))   # Abundant number
        self.assertFalse(is_abundant(15))  # Deficient number
        self.assertFalse(is_abundant(1))   # Border case

    def test_solve_result(self):
        # Solo comprobar que devuelve el resultado correcto conocido
        self.assertEqual(solve(), 4179871)

if __name__ == "__main__":
    unittest.main()
