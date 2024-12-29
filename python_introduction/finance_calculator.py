monthly_income = int(input("Enter the monthly income: "))
total_monthly_expenses= int(input("Enter the total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_annual_savings = annual_savings + interest
print(monthly_savings)
print(projected_annual_savings)