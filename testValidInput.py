import unittest
from main import *

class TestValidInput(unittest.TestCase):
    def test_valid_input(self):
        test_inputs = ["19.99"]
        result = get_valid_input(test_inputs)
        self.assertEqual(result, 19.99, f"Expected 19.99 but got {result}")

    def test_negative_number(self):
        test_inputs = ["-20", "19.99"]
        result = get_valid_input(test_inputs)
        self.assertEqual(result, 19.99, f"Expected 19.99 but got {result}")

    def test_invalid_input(self):
        test_inputs = ["abc", "19.99"]
        result = get_valid_input(test_inputs)
        self.assertEqual(result, 19.99, f"Expected 19.99 but got {result}")

if __name__ == "__main__":
    unittest.main()
