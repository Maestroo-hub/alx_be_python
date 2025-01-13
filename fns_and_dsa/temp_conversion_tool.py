FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Converts temperature from Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts temperature from Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit not in ['C', 'F']:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            return

        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
