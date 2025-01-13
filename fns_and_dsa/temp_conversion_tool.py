# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor for F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor for C to F
FAHRENHEIT_OFFSET = 32  # Offset for Fahrenheit
CELSIUS_OFFSET = 0  # Offset for Celsius


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Using the global conversion factor to convert from Fahrenheit to Celsius
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Using the global conversion factor to convert from Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET


# Main function to interact with the user
def main():
    try:
        # Prompt user for temperature input
        temperature = input("Enter the temperature to convert: ")

        # Check if the input is a valid number
        temperature = float(temperature)

        # Ask user whether the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Validate the unit input
        if unit not in ['C', 'F']:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            return

        # Convert the temperature based on the input unit
        if unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        elif unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")

    except ValueError:
        # Handle case where user input is not a valid number
        print("Invalid temperature. Please enter a numeric value.")


# Run the program
if __name__ == "__main__":
    main()

