import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)       # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)      # Negative and positive numbers
        self.assertEqual(self.calc.add(-5, -3), -8)    # Negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)       # Adding zeros

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.subtract(3, 5), -2) # Subtraction resulting in negative
        self.assertEqual(self.calc.subtract(-5, -3), -2) # Negative numbers
        self.assertEqual(self.calc.subtract(0, 0), 0)   # Subtracting zeros

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)   # Positive numbers
        self.assertEqual(self.calc.multiply(-1, 3), -3)  # Negative and positive numbers
        self.assertEqual(self.calc.multiply(0, 5), 0)   # Multiplying by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6) # Negative numbers

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)     # Division of positive numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)    # Negative and positive numbers
        self.assertEqual(self.calc.divide(0, 5), 0)     # Zero divided by non-zero number
        self.assertEqual(self.calc.divide(5, -5), -1)   # Positive divided by negative
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero (should return None)

    def test_edge_case_divide_by_zero(self):
        """Test division by zero explicitly."""
        self.assertEqual(self.calc.divide(10, 0), None)  # Division by zero should return None
        self.assertEqual(self.calc.divide(0, 0), None)   # Division by zero with zero numerator

if __name__ == '__main__':
    unittest.main()
