monthly_income = int(input("Enter your monthly income: "))
monthly_expenses= int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest
print(monthly_savings)
print(projected_savings)