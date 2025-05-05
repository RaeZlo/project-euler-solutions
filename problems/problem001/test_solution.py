import unittest
from solution import sum_of_multiples

class TestSumOfMultiples(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(sum_of_multiples(10), 23)  

    def test_project_euler_case(self):
        self.assertEqual(sum_of_multiples(1000), 233168)

    def test_zero_case(self):
        self.assertEqual(sum_of_multiples(0), 0)

    def test_negative_limit(self):
        self.assertEqual(sum_of_multiples(-10), 0)

if __name__ == '__main__':
    unittest.main()
