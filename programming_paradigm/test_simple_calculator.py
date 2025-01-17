import unittest
from test_simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)       # Negative and positive numbers
        self.assertEqual(self.calc.add(0, 0), 0)        # Zero case
        self.assertEqual(self.calc.add(-5, -3), -8)     # Negative numbers

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertE
