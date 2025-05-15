import unittest
from solution import is_prime, find_nth_prime 

class TestPrimeFunctions(unittest.TestCase):
    
    def test_is_prime_with_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(29))
    
    def test_is_prime_with_non_primes(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))
    
    def test_find_nth_prime(self):
        self.assertEqual(find_nth_prime(1), 2)
        self.assertEqual(find_nth_prime(2), 3)
        self.assertEqual(find_nth_prime(3), 5)
        self.assertEqual(find_nth_prime(6), 13)
        self.assertEqual(find_nth_prime(10), 29)
        self.assertEqual(find_nth_prime(10001), 104743)

if __name__ == "__main__":
    unittest.main()
