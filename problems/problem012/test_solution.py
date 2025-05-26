import unittest
from solution import count_divisors, first_triangular_with_divisors

class TestTriangularNumber(unittest.TestCase):

    def test_known_small_threshold(self):
        result = first_triangular_with_divisors(5)
        self.assertEqual(result, 28)

    def test_threshold_1(self):
        result = first_triangular_with_divisors(0)
        self.assertEqual(result, 1)

    def test_divisor_count_accuracy(self):
        self.assertGreater(count_divisors(28), 5)

    def test_reasonable_threshold(self):
        result = first_triangular_with_divisors(100)
        self.assertTrue(result > 0)
        self.assertGreater(count_divisors(result), 100)

    def test_large_threshold(self):
        result = first_triangular_with_divisors(300)
        self.assertGreater(count_divisors(result), 300)

if __name__ == '__main__':
    unittest.main()