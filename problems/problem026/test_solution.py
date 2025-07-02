import unittest
from solution import calculate_recurring_cycle_length, find_denominator_with_longest_cycle


class TestRecurringCycle(unittest.TestCase):

    def test_known_cycle_lengths(self):
        # Casos conocidos
        self.assertEqual(calculate_recurring_cycle_length(2), 0)   # 1/2 = 0.5
        self.assertEqual(calculate_recurring_cycle_length(3), 1)   # 1/3 = 0.(3)
        self.assertEqual(calculate_recurring_cycle_length(4), 0)   # 1/4 = 0.25
        self.assertEqual(calculate_recurring_cycle_length(6), 1)   # 1/6 = 0.1(6)
        self.assertEqual(calculate_recurring_cycle_length(7), 6)   # 1/7 = 0.(142857)
        self.assertEqual(calculate_recurring_cycle_length(9), 1)   # 1/9 = 0.(1)

    def test_find_denominator_with_longest_cycle_small_limit(self):
        self.assertEqual(find_denominator_with_longest_cycle(10), 7)
        self.assertEqual(find_denominator_with_longest_cycle(20), 19)

    def test_problem_statement_limit(self):
        self.assertEqual(find_denominator_with_longest_cycle(1000), 983)  # Valor esperado real


if __name__ == '__main__':
    unittest.main()
