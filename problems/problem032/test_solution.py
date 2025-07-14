import unittest
from solution import (
    is_pandigital,
    generate_pandigital_products,
    pandigital_products_sum,
)


class TestPandigitalProducts(unittest.TestCase):
    # ---------- is_pandigital ----------
    def test_is_pandigital_true(self):
        self.assertTrue(is_pandigital("123456789"))

    def test_is_pandigital_false_wrong_length(self):
        self.assertFalse(is_pandigital("12345678"))  # 8 dígitos

    def test_is_pandigital_false_repeated_digits(self):
        self.assertFalse(is_pandigital("112345678"))  # dígito repetido

    # ---------- generate_pandigital_products ----------
    def test_known_identity_present(self):
        products = generate_pandigital_products()
        self.assertIn(7254, products)

    def test_number_of_unique_products(self):
        products = generate_pandigital_products()
        self.assertEqual(len(products), 7)

    # ---------- pandigital_products_sum ----------
    def test_sum_of_products(self):
        self.assertEqual(pandigital_products_sum(), 45228)


if __name__ == "__main__":
    unittest.main()
