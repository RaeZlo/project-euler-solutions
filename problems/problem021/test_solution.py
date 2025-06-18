import unittest
from solution import divisors_sum, amicable_numbers

class TestDivisorsSum(unittest.TestCase):

    def test_divisors_of_1(self):
        self.assertEqual(divisors_sum(1), 0)

    def test_divisors_of_prime(self):
        # 13 es primo, sólo tiene 1 como divisor propio
        self.assertEqual(divisors_sum(13), 1)

    def test_divisors_of_perfect_square(self):
        # 36 tiene divisores propios: 1, 2, 3, 4, 6, 9, 12, 18 → suma: 55
        self.assertEqual(divisors_sum(36), 55)

    def test_divisors_of_even_composite(self):
        # 10 tiene 1, 2, 5 → suma: 8
        self.assertEqual(divisors_sum(10), 8)

    def test_divisors_of_amicable_number_220(self):
        # 220 → divisores propios: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 → suma: 284
        self.assertEqual(divisors_sum(220), 284)

    def test_divisors_of_amicable_number_284(self):
        # 284 → divisores propios: 1, 2, 4, 71, 142 → suma: 220
        self.assertEqual(divisors_sum(284), 220)

class TestAmicableNumbers(unittest.TestCase):

    def test_small_limit(self):
        # Sólo 220 y 284 están antes del 300
        self.assertEqual(amicable_numbers(300), 504)

    def test_no_amicable_numbers(self):
        # Bajo 200 no hay números amigos
        self.assertEqual(amicable_numbers(200), 0)

    def test_known_result(self):
        # Resultado oficial de Project Euler para <10_000
        self.assertEqual(amicable_numbers(10_000), 31626)

if __name__ == '__main__':
    unittest.main()
