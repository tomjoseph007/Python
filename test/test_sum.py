import unittest
from sum import add_two_numbers  # Import the function to be tested

class TestAddTwoNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add_two_numbers(3, 5), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add_two_numbers(-3, -5), -8)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add_two_numbers(-3, 5), 2)
    
    def test_add_zero(self):
        self.assertEqual(add_two_numbers(0, 0), 0)
        self.assertEqual(add_two_numbers(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
