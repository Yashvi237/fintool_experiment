#Practice decision making and loops with financial data
#Created By: Jay Damani
#Date: January 11, 2026

#TASK 1: Account Status Checker
account_balance = 300
if account_balance < 0:
    print("Overdrawn!")
elif account_balance > 0 and account_balance < 500:
    print("Low Balance Warning")
else:
    print("Account Healthy")

#TASK 2: Transaction Classifier
transaction_amount = -300
if transaction_amount < 0:
    print("Expense")
elif transaction_amount > 0:
    print("Income")
else:
    print("Null Transaction")

#TASK 3: Calculate Total Expenses
total = 0
expenses = [-10, -200, -300, -400, -80, -200]
for expense in expenses:
    total += expense

print(f"Total: ${total}")

#TASK 4: Print Each Month's Expense
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
for index,expense in enumerate(expenses):
    print(f"{months[index]}: ${expense}")

#TASK 5: Filter Large Expenses
for index,expense in enumerate(expenses):
    if expense < -100:
        print(f"Large expense in {months[index]}: ${expense}")

#TASK 6: Savings Goal Tracker (CHALLENGE)
current_savings = 0 
goal = 5000
monthly_deposit = 500
month = 0
while current_savings < goal:
    month += 1
    current_savings += monthly_deposit
    print(f"Goal reached in {month} months")