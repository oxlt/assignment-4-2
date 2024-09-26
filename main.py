employee_name = input("Enter employee's name: ")
num_shifts = int(input("Enter number of shifts: "))
num_transactions = int(input("Enter number of transactions: "))
transaction_value = float(input("Enter transaction dollar value: "))

productivity_score = (transaction_value / num_transactions) / num_shifts

bonus = 0

if productivity_score <= 30:
    bonus = 50
if productivity_score > 30 and productivity_score <= 69:
    bonus = 75
if productivity_score > 69 and productivity_score <= 199:
    bonus = 100
if productivity_score > 199:
    bonus = 200

print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus}")