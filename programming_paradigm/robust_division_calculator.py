# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try to convert the inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # This will catch cases where the inputs are not numeric
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # This will catch division by zero errors
        return "Error: Cannot divide by zero."

