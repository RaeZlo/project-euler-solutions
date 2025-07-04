import unittest
from solution import (
    is_prime,
    find_quadratic_coefficients_with_max_primes
)


class TestProblem027(unittest.TestCase):

    def test_is_prime_basic_cases(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))

    def test_is_prime_large_cases(self):
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))
        self.assertTrue(is_prime(7919))
        self.assertFalse(is_prime(7920))

    def test_find_quadratic_coefficients_with_max_primes_default(self):
        self.assertEqual(find_quadratic_coefficients_with_max_primes(), -59231)

    def test_find_quadratic_coefficients_with_max_primes_small_limits(self):
        result = find_quadratic_coefficients_with_max_primes(a_limit=10, b_limit=10)
        self.assertIsInstance(result, int)


if __name__ == '__main__':
    unittest.main()
