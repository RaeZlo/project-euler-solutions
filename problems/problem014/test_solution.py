import unittest
from solution import find_longest_collatz, collatz_length

class TestCollatzFunctions(unittest.TestCase):

    def test_collatz_length_known_values(self):
        cache = {}
        self.assertEqual(collatz_length(1, cache), 1)
        self.assertEqual(collatz_length(2, cache), 2)
        self.assertEqual(collatz_length(13, cache), 11)
        self.assertEqual(collatz_length(9, cache), 22)

    def test_collatz_length_invalid_input(self):
        cache = {}
        with self.assertRaises(ValueError):
            collatz_length(0, cache)
        with self.assertRaises(ValueError):
            collatz_length(-5, cache)

    def test_find_longest_collatz_small_limit(self):
        self.assertEqual(find_longest_collatz(10), 9)
        self.assertEqual(find_longest_collatz(20), 18)

    def test_find_longest_collatz_medium_limit(self):
        result = find_longest_collatz(100_000)
        self.assertTrue(result > 0)

    def test_find_longest_collatz_large_limit(self):
        result = find_longest_collatz(1_000)
        self.assertTrue(result < 1_000)

if __name__ == '__main__':
    unittest.main()
