import unittest
from solution import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(3), 3)
        self.assertEqual(largest_prime_factor(5), 5)

    def test_composite_numbers(self):
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(15), 5)
        self.assertEqual(largest_prime_factor(13195), 29) 

    def test_large_number(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)  

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            largest_prime_factor(1)

if __name__ == '__main__':
    unittest.main()