import unittest
from calculate_change import calculate_change

class TestCalculateChange(unittest.TestCase):
    def test_exact_ten_dollars(self):
        result = calculate_change(10.00)
        expected = {
            'bills': {'$10': 1, '$5': 0, '$1': 0},
            'coins': {'quarters': 0, 'dimes': 0, 'pennies': 0}
        }
        self.assertEqual(result, expected)

    def test_nineteen_ninety_nine(self):
        result = calculate_change(19.99)
        expected = {
            'bills': {'$10': 1, '$5': 1, '$1': 4},
            'coins': {'quarters': 3, 'dimes': 2, 'pennies': 4}
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
