Task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
Time_bound = str(input("Is it time-bound? (yes/no): "))

#  match priority:
       # case "high":
       # if time_bound == "yes":
          
match priority.lower() and Time_bound.lower():
    case "high" | "medium" | "low":
        if Time_bound.lower() == "yes" and (priority.lower() == "high" or priority.lower() == "medium" or priority.lower() == "low"):
            print(f"Reminder: {Task} is a {priority} priority task that requires immediate attention today!.")
        elif Time_bound.lower() == "no" and (priority.lower() == "high" or priority.lower() == "medium" or priority.lower() == "low"):
            print(f"Reminder: {Task} is a {priority} priority task conside completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low \n " \
        "Don't forget to fill in the Time Bound space. \n Lower case is preferred for priority and time bound inputs.")