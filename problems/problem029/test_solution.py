import unittest
from solution import distinct_powers

class TestDistinctPowers(unittest.TestCase):

    def test_default_case(self):
        self.assertEqual(distinct_powers(), 9183)

    def test_small_range(self):
        self.assertEqual(distinct_powers(5, 5), 15)  # Resultado esperado: 15 términos distintos

    def test_minimum_range(self):
        self.assertEqual(distinct_powers(2, 2), 1)  # Solo 2^2 = 4

    def test_single_base_multiple_exponents(self):
        self.assertEqual(distinct_powers(2, 5), 4)  # 2^2, 2^3, 2^4, 2^5

    def test_multiple_bases_single_exponent(self):
        self.assertEqual(distinct_powers(5, 2), 4)  # 2^2=4, 3^2=9, 4^2=16, 5^2=25

    def test_duplicates(self):
        self.assertEqual(distinct_powers(4, 4), 8)  # 2^2, 2^3, 2^4, 3^2, 3^3, 3^4, 4^2, 4^3, 4^4

    def test_large_single_case(self):
        self.assertEqual(distinct_powers(10, 10), len({a ** b for a in range(2, 11) for b in range(2, 11)}))

if __name__ == '__main__':
    unittest.main()
