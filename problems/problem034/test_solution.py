import unittest
from solution import digit_factorial_sum, factorial

class TestDigitFactorialSum(unittest.TestCase):

    def test_known_result(self):
        """Test del resultado total conocido para el límite por defecto."""
        self.assertEqual(digit_factorial_sum(), 40730)

    def test_custom_upper_bound(self):
        """Test con un límite más pequeño, donde no debe haber resultados."""
        self.assertEqual(digit_factorial_sum(100), 0)

    def test_exact_matches(self):
        """Test de casos conocidos que sí cumplen la condición."""
        matches = []
        for n in range(10, 150):
            if n == sum(factorial(int(d)) for d in str(n)):
                matches.append(n)
        self.assertIn(145, matches)
        self.assertEqual(matches, [145])

if __name__ == '__main__':
    unittest.main()
