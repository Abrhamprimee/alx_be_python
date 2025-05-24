imonthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

# Ensure correct variable assignment
monthly_savings = monthly_income - monthly_expenses

print("Your monthly savings are: $", monthly_savings)

project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest: $", project_savings)
