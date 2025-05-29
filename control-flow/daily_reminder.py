Task = str(input("Enter your task: "))
Priority = str(input("Priority (high/medium/low): "))
Time_bound = str(input("Is it time-bound? (yes/no): "))

match Priority.lower() and Time_bound.lower():
    case "high" | "medium" | "low":
        if Time_bound.lower() == "yes" and (Priority.lower() == "high" or Priority.lower() == "medium" or Priority.lower() == "low"):
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!.")
        elif Time_bound.lower() == "no" and (Priority.lower() == "high" or Priority.lower() == "medium" or Priority.lower() == "low"):
            print(f"Reminder: {Task} is a {Priority} priority task conside completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low \n " \
        "Don't forget to fill in the Time Bound space. \n Lower case is preferred for priority and time bound inputs.")