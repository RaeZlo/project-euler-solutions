import unittest
from solution import is_prime, sum_prime

class TestProjectEuler010(unittest.TestCase):

    def test_is_prime_basic(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(25))
        self.assertTrue(is_prime(29))

    def test_sum_prime_small_range(self):
        self.assertEqual(sum_prime(0), 0)
        self.assertEqual(sum_prime(1), 0)
        self.assertEqual(sum_prime(2), 0)     
        self.assertEqual(sum_prime(10), 17)  
        self.assertEqual(sum_prime(20), 77)   

    def test_sum_prime_medium_range(self):
        self.assertEqual(sum_prime(100), 1060)
        self.assertEqual(sum_prime(200), 4227)

if __name__ == '__main__':
    unittest.main()