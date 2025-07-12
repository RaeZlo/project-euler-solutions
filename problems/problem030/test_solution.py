import unittest
from solution import digit_fifth_powers

class TestDigitFifthPowers(unittest.TestCase):
    # --- Casos básicos y valor esperado -------------------------------

    def test_default_power(self):
        """power = 5 debe devolver el resultado conocido de Project Euler #30."""
        self.assertEqual(digit_fifth_powers(), 443_839)

    def test_power_four(self):
        """power = 4 (cuarta potencia) -- números de Armstrong de 4º orden."""
        self.assertEqual(digit_fifth_powers(4), 19_316)

    def test_power_three(self):
        """power = 3 -- números de Armstrong (153, 370, 371, 407)."""
        self.assertEqual(digit_fifth_powers(3), 1_301)

    # --- Casos límite / bordes ----------------------------------------

    def test_power_zero(self):
        """power = 0 -- ningún número cumple (resultado debe ser 0)."""
        self.assertEqual(digit_fifth_powers(0), 0)

    def test_small_search_space(self):
        """power > 5 todavía debe ejecutarse y retornar un int (no falla)."""
        result = digit_fifth_powers(6)         # No se comprueba el valor exacto
        self.assertIsInstance(result, int)     # pero sí que retorna un entero

    # --- Robustez del tipo de retorno ---------------------------------

    def test_return_type(self):
        """Siempre debería devolver un int, incluso con potencias negativas."""
        self.assertIsInstance(digit_fifth_powers(-1), int)

if __name__ == '__main__':
    unittest.main()
