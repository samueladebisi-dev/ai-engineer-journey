import json
import os


if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
else:
    expenses = []
    
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

def add_expense(expenses):
    name = input("Expense name: ")
    amount = float(input("Amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    return expenses

total = sum(expense["amount"] for expense in expenses)

print(f"\nTotal Spent: ₦{total}")


with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

category = input("Category: ")


expenses.append({
    "name": name,
    "amount": amount,
    "category": category
})

print(
    f"{expense['name']} | "
    f"{expense['category']} | "
    f"₦{expense['amount']}"
)
