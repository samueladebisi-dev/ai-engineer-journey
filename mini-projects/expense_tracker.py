import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Expense name: ")
    category = input("Category: ")

    while True:
        try:
            amount = float(input("Amount: ₦"))
            break
        except ValueError:
            print("Please enter a valid amount.")

    expenses.append({
        "name": name,
        "category": category,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense added successfully.\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return

    total = 0

    print("\nExpenses")
    print("-" * 40)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} | "
            f"{expense['category']} | "
            f"₦{expense['amount']:.2f}"
        )
        total += expense["amount"]

    print("-" * 40)
    print(f"Total Expenses: ₦{total:.2f}")
    print(f"Number of Entries: {len(expenses)}")
    print(f"Average Expense: ₦{total / len(expenses):.2f}\n")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.\n")
        return

    view_expenses(expenses)

    try:
        index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses(expenses)
            print(f"{deleted['name']} deleted successfully.\n")
        else:
            print("Invalid expense number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def edit_expense(expenses):
    if not expenses:
        print("No expenses available.\n")
        return

    view_expenses(expenses)

    try:
        index = int(input("Enter expense number to edit: ")) - 1

        if 0 <= index < len(expenses):
            expenses[index]["name"] = input("New name: ")
            expenses[index]["category"] = input("New category: ")

            while True:
                try:
                    expenses[index]["amount"] = float(
                        input("New amount: ₦")
                    )
                    break
                except ValueError:
                    print("Please enter a valid amount.")

            save_expenses(expenses)
            print("Expense updated successfully.\n")

        else:
            print("Invalid expense number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def search_expense(expenses):
    if not expenses:
        print("No expenses available.\n")
        return

    keyword = input("Search: ").lower()

    found = False

    print()

    for expense in expenses:
        if (
            keyword in expense["name"].lower()
            or keyword in expense["category"].lower()
        ):
            print(
                f"{expense['name']} | "
                f"{expense['category']} | "
                f"₦{expense['amount']:.2f}"
            )
            found = True

    if not found:
        print("No matching expenses found.")

    print()


expenses = load_expenses()

while True:
    print("====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Edit Expense")
    print("5. Search Expense")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        delete_expense(expenses)

    elif choice == "4":
        edit_expense(expenses)

    elif choice == "5":
        search_expense(expenses)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.\n")