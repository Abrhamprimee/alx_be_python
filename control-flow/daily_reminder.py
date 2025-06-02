# daily_reminder.py

def get_task_info():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    reminder = f"Reminder: '{task}' is a "

    match priority:
        case "high":
            reminder += "high priority task"
        case "medium":
            reminder += "medium priority task"
        case "low":
            reminder += "low priority task"
        case _:
            reminder += "task of unspecified priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    return reminder

if __name__ == "__main__":
    task, priority, time_bound = get_task_info()
    print(generate_reminder(task, priority, time_bound))
