import datetime


def display_current_datetime():
    current_datetime = datetime.datetime.now()

    formatted_current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_current_datetime}")
    return formatted_current_datetime


def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    current_date = datetime.datetime.now().date()

    future_date = current_date + datetime.timedelta(days=days_to_add)

    print(f"Future date: {future_date}")
    return future_date


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

