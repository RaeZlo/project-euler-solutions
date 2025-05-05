import unittest
from solution import sum_even_fibonacci

class TestSumEvenFibonacci(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(sum_even_fibonacci(89), 44)

    def test_limit_case(self):
        self.assertEqual(sum_even_fibonacci(4_000_000), 4613732)

    def test_no_even_numbers(self):
        self.assertEqual(sum_even_fibonacci(1), 0)

    def test_edge_case(self):
        self.assertEqual(sum_even_fibonacci(2), 2)

if __name__ == "__main__":
    unittest.main()