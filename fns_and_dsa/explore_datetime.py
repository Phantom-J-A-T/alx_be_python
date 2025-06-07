from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") # Make Datetime readable
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a future date
def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Main program
if __name__ == "__main__":
    display_current_datetime()

    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer number of days.")
