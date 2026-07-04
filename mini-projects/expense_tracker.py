from utils import save_json, load_json
from config import DATA_FILE
import os


if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        expenses = json.load(file)
else:
    expenses = []
    
expenses = []


def display_expense(expense: dict) -> None:
    print(
        f"{expense['name']} | "
        f"{expense['category']} | "
        f"₦{expense['amount']}"
    )

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
            display_expense(expense)

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


with open(DATA_FILE, "w") as file:
    json.dump(expenses, file, indent=4)

category = input("Category: ")


expenses.append({
    "name": name,
    "amount": amount,
    "category": category
})

