student_name = input("What is your name: ")
scholarship = int(input("Your Scholarship: "))
part_time = int(input("How much you earn from your part time job: "))
monthly_income = scholarship + part_time
dorm_money = int(input("How much you pay for rent?: "))
meal_money = int(input (" Your average cost for meal: "))
textbook_money = int(input("How much you spend for your textbooks: "))
fixed_expense = dorm_money + meal_money + textbook_money
personal_expense = int(input("How much you spend for personal expenses like self-caring, transport : "))
total_expense = personal_expense + fixed_expense
balance = int(input("How you have in your balance: "))
net_savings = monthly_income - total_expense
expense_income_ratio = total_expense/monthly_income

status = (balance >= 0 and "No Student loan") or "Student loan exists"
critical = (expense_income_ratio > 0.95 and "Critical") or "Not Critical"
risky = ( expense_income_ratio>0.85 and expense_income_ratio <=0.95 and "Risky") or "Not risky"
healthy = ( expense_income_ratio <= 0.70 and "healthy") or " Unhealthy"
rate_percentage = total_expense/monthly_income * 100
fund_goal = int(input("Amount of emergency fund: "))
fund = ( net_savings >= fund_goal and "Adequate fund") or "Inadequate fund"
months_fund_goal = fund_goal / net_savings
fund_gap = fund_goal - net_savings
recommended_savings = monthly_income/100 * 15
print(f'\n{"="*50}')
print("Student Living Expenses Tracker")
print(f'\n{"="*50}')
print(f'Student name: {student_name}')
print(f'Monthly income: {monthly_income}')
print(f'Total Expenses: {total_expense}')
print(f'Saving balance: {balance}')
print(f'Student loan : {status}')
print(f'{"-"*50}')
print(f'Rate Percentage of Savings: {rate_percentage:.2f}')
print(f'Expense to Income ratio: {expense_income_ratio:.2f}')
print(f'\n{"="*50}')
print(f'Months to reach fund goal: {months_fund_goal:.2f}')
print(f'Emergency fund gap goal: {fund_gap}')
print(f'Recommended savings: {recommended_savings}')



