task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority and time bound task "
                   f"that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. "
                  f"Do it as soon as possible!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority and time bound task. "
                  f"Complete it soon")
        else:
            print(f"Reminder: '{task}' is a medium priority task. ")
    case "low":
        message = f"Note: '{task}' is a low priority task. "
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority and time bound task. "
                  f"Do it at some time.")
        else:
            print(f"Note: '{task}' is a low priority  task. "
              f"Consider completing it when you have free time.")
    case _:
        print("Invalid input.")