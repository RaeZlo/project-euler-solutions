import unittest
from solution import count_letter_length, total_letter_count, NUM_WORDS

class TestLetterCount(unittest.TestCase):

    def test_single_digits(self):
        self.assertEqual(count_letter_length(1, NUM_WORDS), 3)  # "one"
        self.assertEqual(count_letter_length(9, NUM_WORDS), 4)  # "nine"

    def test_teens(self):
        self.assertEqual(count_letter_length(11, NUM_WORDS), 6)  # "eleven"
        self.assertEqual(count_letter_length(19, NUM_WORDS), 8)  # "nineteen"

    def test_exact_tens(self):
        self.assertEqual(count_letter_length(20, NUM_WORDS), 6)  # "twenty"
        self.assertEqual(count_letter_length(90, NUM_WORDS), 6)  # "ninety"

    def test_tens_with_units(self):
        self.assertEqual(count_letter_length(21, NUM_WORDS), 9)  # "twentyone"
        self.assertEqual(count_letter_length(42, NUM_WORDS), 8)  # "fortytwo"

    def test_exact_hundreds(self):
        self.assertEqual(count_letter_length(100, NUM_WORDS), 10)  # "onehundred"
        self.assertEqual(count_letter_length(300, NUM_WORDS), 12)  # "threehundred"

    def test_hundreds_with_remainder(self):
        self.assertEqual(count_letter_length(115, NUM_WORDS), 20)  # "onehundredandfifteen"
        self.assertEqual(count_letter_length(342, NUM_WORDS), 23)  # "threehundredandfortytwo"

    def test_one_thousand(self):
        self.assertEqual(count_letter_length(1000, NUM_WORDS), 11)  # "onethousand"

    def test_invalid_numbers(self):
        with self.assertRaises(ValueError):
            count_letter_length(0, NUM_WORDS)
        with self.assertRaises(ValueError):
            count_letter_length(1001, NUM_WORDS)
        with self.assertRaises(ValueError):
            count_letter_length(-5, NUM_WORDS)

    def test_total_letter_count(self):
        # Este es el resultado conocido del problema 17 de Project Euler
        self.assertEqual(total_letter_count(5), 19)     # one(3)+two(3)+three(5)+four(4)+five(4)
        self.assertEqual(total_letter_count(1000), 21124)  # respuesta conocida del problema


if __name__ == '__main__':
    unittest.main()
