import datetime


def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
    """
    Calculates the future date by adding a given number of days to the current date.
    :param days: Number of days to add
    :return: Future date in "YYYY-MM-DD" format
    """
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    display_current_datetime()

    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")


if __name__ == "__main__":
    main()
