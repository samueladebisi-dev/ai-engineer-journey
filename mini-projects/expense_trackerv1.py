expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))

        expenses.append({
            "name": name,
            "amount": amount
        })

    elif choice == "2":
        for expense in expenses:
            print(f"{expense['name']} - ₦{expense['amount']}")

    elif choice == "3":
        break

total = sum(expense["amount"] for expense in expenses)

print(f"\nTotal Spent: ₦{total}")
