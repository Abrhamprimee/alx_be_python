income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))

savings = income - expenses
print("Your monthly savings are: $", savings)

project_savings = savings * 12 + (savings * 12 * 0.05)
print("Projected savings after one year, with interest: $", project_savings)
