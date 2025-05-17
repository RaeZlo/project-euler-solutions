import unittest
from solution import find_pythagorean_triplet_product

class TestPythagoreanTriplet(unittest.TestCase):
    
    def test_default_total(self):
        self.assertEqual(find_pythagorean_triplet_product(1000), 31875000)
    
    def test_total_12(self):
        self.assertEqual(find_pythagorean_triplet_product(12), 60)
    
    def test_impossible_total(self):
        self.assertEqual(find_pythagorean_triplet_product(5), -1)
    
    def test_total_100(self):
        self.assertEqual(find_pythagorean_triplet_product(100), -1)

if __name__ == "__main__":
    unittest.main()