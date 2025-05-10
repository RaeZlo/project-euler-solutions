import unittest
from solution import largest_palindrome_product, is_palindrome

class TestPalindromeProduct(unittest.TestCase):
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(9009))
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(0))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(12310))

    def test_largest_palindrome_default_range(self):
        result = largest_palindrome_product()
        self.assertEqual(result, 906609)

    def test_largest_palindrome_small_range(self):
        result = largest_palindrome_product(10, 99)
        self.assertEqual(result, 9009)

    def test_largest_palindrome_single_value_range(self):
        result = largest_palindrome_product(11, 11)
        self.assertEqual(result, 121)

    def test_largest_palindrome_no_palindrome(self):
        result = largest_palindrome_product(10, 10)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
    