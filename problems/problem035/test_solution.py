import unittest
from solution import is_prime, list_primes, get_rotations, circular_primes

class TestEulerProblem35(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(100))

    def test_list_primes(self):
        self.assertEqual(list_primes(10), [2, 3, 5, 7])
        self.assertIn(29, list_primes(30))
        self.assertNotIn(30, list_primes(30))

    def test_get_rotations(self):
        self.assertEqual(get_rotations(197), [197, 971, 719])
        self.assertEqual(get_rotations(101), [101, 11, 110])
        self.assertEqual(get_rotations(11), [11, 11])
        self.assertEqual(get_rotations(7), [7])

    def test_circular_primes_limit_100(self):
        self.assertEqual(circular_primes(100), 13)  # Confirmado por el sitio de Project Euler

    def test_circular_primes_limit_1(self):
        self.assertEqual(circular_primes(1), 0)

    def test_circular_primes_limit_2(self):
        self.assertEqual(circular_primes(2), 0)  # Porque no hay primos < 2

if __name__ == '__main__':
    unittest.main()
