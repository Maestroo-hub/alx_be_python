import unittest

class SimpleCalculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return None  # Handle division by zero by returning None
        return a / b


from simple_calculators import SimpleCalculator

class SimpleCalculator(unittest.TestCase):



    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.addition(2, 3), 5)        # Positive numbers
        self.assertEqual(self.calc.addition(-1, 1), 0)       # Negative and positive numbers
        self.assertEqual(self.calc.addition(0, 0), 0)        # Zero case
        self.assertEqual(self.calc.addition(-5, -3), -8)     # Negative numbers

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtraction(5, 3), 2)
        self.assertEqual(self.calc.subtraction(-1, 1), -2)
        self.assertEqual(self.calc.subtraction(0, 0), 0)
        self.assertEqual(self.calc.subtraction(-1, -1), 2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiplication(5, 3), 15)
        self.assertEqual(self.calc.multiplication(-1, 1), -1)
        self.assertEqual(self.calc.multiplication(0, 0), 0)
        self.assertEqual(self.calc.multiplication(-1, -1), 1)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.division(6, 3), 2)
        self.assertEqual(self.calc.division(5, 2), 2.5)
        self.assertEqual(self.calc.division(-6, 3), -2)
        self.assertEqual(self.calc.division(7, 2), 3.5)
        self.assertEqual(self.calc.division(0, 5), 0)

        # Test division by zero
        self.assertIsNone(self.calc.division(5, 0))  # Check that dividing by zero returns None
        self.assertIsNone(self.calc.division(-5, 0))  # Check division by zero with negative number

if __name__ == '__main__':
    unittest.main()