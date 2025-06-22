import unittest
from solution import find_nth_permutation

class TestLexicographicPermutation(unittest.TestCase):

    def test_basic_cases(self):
        digits = ['0', '1', '2']
        self.assertEqual(find_nth_permutation(digits, 1), '012')  # 1st
        self.assertEqual(find_nth_permutation(digits, 2), '021')
        self.assertEqual(find_nth_permutation(digits, 3), '102')
        self.assertEqual(find_nth_permutation(digits, 4), '120')
        self.assertEqual(find_nth_permutation(digits, 5), '201')
        self.assertEqual(find_nth_permutation(digits, 6), '210')  # last

    def test_error_too_small(self):
        digits = ['0', '1', '2']
        with self.assertRaises(IndexError):
            find_nth_permutation(digits, 0)  # Invalid: below range

    def test_error_too_large(self):
        digits = ['0', '1', '2']
        with self.assertRaises(IndexError):
            find_nth_permutation(digits, 7)  # Invalid: above 3! = 6

    def test_single_digit(self):
        self.assertEqual(find_nth_permutation(['7'], 1), '7')
        with self.assertRaises(IndexError):
            find_nth_permutation(['7'], 2)

    def test_two_digits(self):
        digits = ['a', 'b']
        self.assertEqual(find_nth_permutation(digits, 1), 'ab')
        self.assertEqual(find_nth_permutation(digits, 2), 'ba')

    def test_four_digits_middle_case(self):
        digits = ['1', '2', '3', '4']
        self.assertEqual(find_nth_permutation(digits, 12), '2431')  # 12th out of 24

    def test_large_case_problem_24(self):
        digits = [str(d) for d in range(10)]
        result = find_nth_permutation(digits, 1_000_000)
        self.assertEqual(result, "2783915460")

    def test_n_equals_factorial_length(self):
        digits = ['0', '1', '2', '3']
        # 4! = 24 permutations → last one
        self.assertEqual(find_nth_permutation(digits, 24), '3210')

    def test_reverse_digits(self):
        digits = ['3', '2', '1', '0']
        self.assertEqual(find_nth_permutation(digits, 1), '0123')  # Sorted internally

if __name__ == '__main__':
    unittest.main()
