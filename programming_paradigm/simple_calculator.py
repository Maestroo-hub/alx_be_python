# from urllib.response import addbase

class SimpleCalculator:
 """A simple calculator class that supports basic arithmetic operations."""

def add(a, b):
    # Return the addition of a and b.
    return a + b

def subtract(a, b):
    # Return the subtraction of a and b.
    return a - b

def multiply(a, b):
    # Return the multiplication of a and b.
    return a * b

def divide(a, b):
    # Return the division of a by b. Returns None if b is zero
    if b == 0:
        return None
    return a / b