import unittest

class SimpleCalculator:
    pass


from test_simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, -1), 1)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subt(5, 3),2)
        self.assertEqual(self.calc.subt(-1, 1), -2)
        self.assertEqual(self.calc.subt(-1, -1), 0)

        # Add more assertions to thoroughly test the add method.
