import unittest
from solution import coin_sums

class TestCoinSums(unittest.TestCase):
    # --- Casos básicos -----------------------------------------------------
    def test_example_project_euler(self):
        coins = [1, 2, 5, 10, 20, 50, 100, 200]
        self.assertEqual(coin_sums(200, coins), 73682)

    def test_small_target_simple_coins(self):
        self.assertEqual(coin_sums(5, [1, 2]), 3)   # 5, 2+1+1+1, 2+2+1

    # --- Casos límite / bordes --------------------------------------------
    def test_target_zero(self):
        self.assertEqual(coin_sums(0, [1, 5, 10]), 1)

    def test_single_coin_equal_target(self):
        self.assertEqual(coin_sums(7, [7]), 1)

    def test_single_coin_smaller_than_target(self):
        self.assertEqual(coin_sums(4, [2]), 1)  # 2+2

    # --- Escenarios vacíos / irrelevantes ----------------------------------
    def test_no_coins(self):
        self.assertEqual(coin_sums(10, []), 0)
        self.assertEqual(coin_sums(0, []), 1)

    def test_all_coins_bigger_than_target(self):
        self.assertEqual(coin_sums(3, [5, 7, 11]), 0)

    # --- Robustez: valores repetidos o desordenados ------------------------
    def test_duplicates_and_unordered_coins(self):
        self.assertEqual(
            coin_sums(4, [2, 1, 2, 1]),  # duplicados
            coin_sums(4, [1, 2])         # resultado esperado: 3
        )

    # --- Valores grandes pero viables --------------------------------------
    def test_large_target_small_coin_set(self):
        self.assertEqual(coin_sums(1000, [1, 5, 10, 25]), 142511)

    # --- Validación de entrada (opcional) ----------------------------------
    def test_negative_target_raises_value_error(self):
        with self.assertRaises(ValueError):
            coin_sums(-5, [1, 2, 5])

if __name__ == "__main__":
    unittest.main()
