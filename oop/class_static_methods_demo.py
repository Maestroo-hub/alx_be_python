class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method - does not need access to class or instance attributes
    @staticmethod
    def add(a, b):
        return a + b

    # Class method - needs access to the class (cls)
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
