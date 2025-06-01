task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task "
        if time_bound == "yes":
            message += "that requires immediate attention today!"
        print(f"{message}")
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task. "
        if time_bound == "yes":
            message += "Its good to do today!"
        print(f"{message}")
    case "low":
        message = f"Note: '{task}' is a low priority task. "
        if time_bound == "no":
            message += "Consider completing it when you have free time."
        print(f"{message}")
    case _:
        print("Sorry, I didn't understand that.")