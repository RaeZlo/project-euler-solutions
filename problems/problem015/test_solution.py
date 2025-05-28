import unittest
from solution import binomial_coefficient

class TestBinomialCoefficient(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(binomial_coefficient(5, 2), 10)
        self.assertEqual(binomial_coefficient(10, 3), 120)
        self.assertEqual(binomial_coefficient(6, 0), 1)
        self.assertEqual(binomial_coefficient(6, 6), 1)

    def test_symmetry(self):
        self.assertEqual(binomial_coefficient(10, 3), binomial_coefficient(10, 7))
        self.assertEqual(binomial_coefficient(20, 8), binomial_coefficient(20, 12))

    def test_large_values(self):
        self.assertEqual(binomial_coefficient(20, 10), 184756)
        self.assertEqual(binomial_coefficient(30, 15), 155117520)

    def test_invalid_cases(self):
        self.assertEqual(binomial_coefficient(5, 6), 0)
        self.assertEqual(binomial_coefficient(0, 1), 0)

    def test_zero_case(self):
        self.assertEqual(binomial_coefficient(0, 0), 1)

    def test_edge_k_equals_one_or_n_minus_1(self):
        self.assertEqual(binomial_coefficient(10, 1), 10)
        self.assertEqual(binomial_coefficient(10, 9), 10)

    def test_type_and_range_checking(self):
        with self.assertRaises(TypeError):
            binomial_coefficient("5", "2")

        with self.assertRaises(TypeError):
            binomial_coefficient(5.0, 2.0)

if __name__ == '__main__':
    unittest.main()
