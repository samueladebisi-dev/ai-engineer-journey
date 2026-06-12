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
