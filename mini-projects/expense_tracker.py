expenses = []

while True:
    amount = input("Enter expense (or quit): ")

    if amount.lower() == "quit":
        break

    expenses.append(float(amount))
    
print("Total Expenses:", sum(expenses))
print("Number of Entries:", len(expenses))
