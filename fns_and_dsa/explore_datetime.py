from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now().replace(microsecond=0, second=(datetime.now().second // 10) * 10)
    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))


display_current_datetime()
calculate_future_date()