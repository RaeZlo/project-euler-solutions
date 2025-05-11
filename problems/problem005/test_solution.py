import unittest
from solution import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
    def test_example_case(self):
        # Test con el límite 10, el resultado esperado es 2520
        self.assertEqual(smallest_multiple(10), 2520)

    def test_project_euler_case(self):
        # Test con el límite 20, el resultado esperado es 232792560
        self.assertEqual(smallest_multiple(20), 232792560)

    def test_zero_case(self):
        # Test para el límite 0, el menor múltiplo común para el rango 1 hasta 0 es 0
        self.assertEqual(smallest_multiple(0), 0)

    def test_negative_limit(self):
        # Test para un límite negativo, donde no tiene sentido calcular el MCM
        self.assertEqual(smallest_multiple(-10), 0)

if __name__ == '__main__':
    unittest.main()
