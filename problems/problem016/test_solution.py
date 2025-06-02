import unittest
from solution import power_digit_sum

class TestPowerDigitSum(unittest.TestCase):

    def test_small_power(self):
        # 2^15 = 32768 → 3+2+7+6+8 = 26
        self.assertEqual(power_digit_sum(2, 15), 26)

    def test_main_problem(self):
        # 2^1000 → suma esperada: 1366
        self.assertEqual(power_digit_sum(2, 1000), 1366)

    def test_base_10_power_3(self):
        # 10^3 = 1000 → 1 + 0 + 0 + 0 = 1
        self.assertEqual(power_digit_sum(10, 3), 1)

    def test_zero_exponent(self):
        # Cualquier número elevado a 0 da 1 → suma de dígitos = 1
        self.assertEqual(power_digit_sum(7, 0), 1)
        self.assertEqual(power_digit_sum(0, 0), 1)  # Por convención matemática

    def test_zero_base(self):
        # 0^n = 0 para n > 0 → suma de dígitos = 0
        self.assertEqual(power_digit_sum(0, 5), 0)

    def test_large_base_and_exponent(self):
        # No validamos el número sino que no falle y dé un resultado entero
        result = power_digit_sum(99, 100)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_negative_base(self):
        # (-2)^3 = -8 → suma de dígitos = 8
        self.assertEqual(power_digit_sum(-2, 3), 8)
        # (-2)^4 = 16 → suma = 1+6=7
        self.assertEqual(power_digit_sum(-2, 4), 7)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            power_digit_sum("2", 5)
        with self.assertRaises(TypeError):
            power_digit_sum(2, "5")
        with self.assertRaises(TypeError):
            power_digit_sum(None, 5)

if __name__ == "__main__":
    unittest.main()
