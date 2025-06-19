import unittest
from unittest.mock import mock_open, patch
from solution import (
    load_and_sort_names,
    alphabetical_value,
    total_name_scores
)


class TestProblem022(unittest.TestCase):

    def test_alphabetical_value_single_letter(self):
        self.assertEqual(alphabetical_value("A"), 1)
        self.assertEqual(alphabetical_value("Z"), 26)

    def test_alphabetical_value_word(self):
        self.assertEqual(alphabetical_value("COLIN"), 53)  # C(3)+O(15)+L(12)+I(9)+N(14)

    def test_load_and_sort_names(self):
        mock_data = '"MARY","PATRICIA","LINDA","BARBARA","ELIZABETH"'
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = load_and_sort_names("fake_path.txt")
            self.assertEqual(result, ['BARBARA', 'ELIZABETH', 'LINDA', 'MARY', 'PATRICIA'])

    def test_total_name_scores_with_mock_file(self):
        mock_data = '"MARY","PATRICIA","LINDA"'
        # Orden alfabético: LINDA, MARY, PATRICIA
        # LINDA: 12+9+14+4+1 = 40 → pos 1 → 40
        # MARY: 13+1+18+25 = 57 → pos 2 → 114
        # PATRICIA: 16+1+20+18+9+3+9+1 = 77 → pos 3 → 231
        expected_total = 40 + 114 + 231  # = 385

        with patch("builtins.open", mock_open(read_data=mock_data)):
            total = total_name_scores("fake_path.txt")
            self.assertEqual(total, expected_total)

    def test_empty_file(self):
        with patch("builtins.open", mock_open(read_data="")):
            result = load_and_sort_names("empty.txt")
            self.assertEqual(result, [])
            total = total_name_scores("empty.txt")
            self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
