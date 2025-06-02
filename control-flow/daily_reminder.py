# Personal Daily Reminder

task = input("Enter your task: ")  # Input the task
priority = input("Priority (High/Medium/Low): ").strip().capitalize()  # Normalize input formatting
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()  # Normalize input formatting

match priority:
    case "High":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "Medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "Low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered."

# Adjust reminder if the task is time-sensitive
if time_bound == "yes" and priority in ["High", "Medium", "Low"]:
    reminder += " It requires immediate attention today!"

print(reminder)
