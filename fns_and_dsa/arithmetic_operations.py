def perform_operation(num1, num2, operation):
    """
    Perform the requested arithmetic operation on two numbers.

    :param num1: First number
    :param num2: Second number
    :param operation: Operation to perform (add, subtract, multiply, divide)
    :return: The result of the operation
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
