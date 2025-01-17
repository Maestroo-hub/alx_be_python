# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time in a readable format
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Ask the user to input the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date by adding days to the current date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Main function to call the parts
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()


