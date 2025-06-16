import unittest
from solution import is_leap_year, count_sundays_on_first

class TestProblem019(unittest.TestCase):

    # Tests para is_leap_year
    def test_common_leap_year(self):
        self.assertTrue(is_leap_year(1996))  # divisible por 4, no por 100

    def test_century_non_leap_year(self):
        self.assertFalse(is_leap_year(1900))  # divisible por 100, no por 400

    def test_century_leap_year(self):
        self.assertTrue(is_leap_year(2000))  # divisible por 400

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(1999))  # no divisible por 4

    # Tests para count_sundays_on_first
    def test_full_twentieth_century(self):
        self.assertEqual(count_sundays_on_first(), 171)  # Problema original

    def test_single_year_range(self):
        # Verificamos cuántos domingos hubo en primeros del mes en 1901
        # Manualmente se verifica que son 2 (septiembre y diciembre)
        self.assertEqual(count_sundays_on_first(1901, 1901), 2)

    def test_small_range(self):
        # Comprobamos rango de 1901 a 1903
        result = count_sundays_on_first(1901, 1903)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)

    def test_reverse_range(self):
        # Rango invertido debe retornar 0
        self.assertEqual(count_sundays_on_first(2000, 1901), 0)

    def test_exact_known_result(self):
        # 1 Jan 1901 fue martes. 1 Dec 1901 fue domingo.
        # Así que al menos diciembre 1901 debe contar como domingo.
        self.assertGreaterEqual(count_sundays_on_first(1901, 1901), 1)


if __name__ == "__main__":
    unittest.main()
