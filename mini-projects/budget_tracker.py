income = float(input("Enter income: "))
expenses = float(input("Enter expenses: "))

balance = income - expenses

print("Remaining balance:", balance)

if balance > 0:
    print("You are saving money.")
elif balance < 0:
    print("You spent more than you earned.")
else:
    print("You broke even.")

savings_rate = (balance / income) * 100

print("Savings Rate:", round(savings_rate, 2), "%")
