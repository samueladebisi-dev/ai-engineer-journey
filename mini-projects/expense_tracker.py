import json
from config import DATA_FILE
from exceptions import InvalidExpenseError
import os


def display_menu() -> None:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")


def display_expense(expense: dict) -> None:
    print(
        f"{expense['name']} | "
        f"{expense['category']} | "
        f"₦{expense['amount']:.2f}"
    )


def calculate_total(expenses: list[dict]) -> float:
    return sum(expense["amount"] for expense in expenses)


def load_expenses() -> list[dict]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses: list[dict]) -> None:
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses: list[dict]) -> None:
    name = input("Expense name: ")

    try:
        amount = float(input("Amount: "))

        if amount < 0:
            raise InvalidExpenseError("Expense amount cannot be negative.")

    except ValueError:
        print("Please enter a valid number.")
        return

    except InvalidExpenseError as e:
        print(e)
        return

    category = input("Category: ")

    expenses.append(
        {
            "name": name,
            "amount": amount,
            "category": category,
        }
    )

    save_expenses(expenses)

    print("Expense added successfully.")


def view_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses found.")
        return

    print()

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. ", end="")
        display_expense(expense)
    
    total = calculate_total(expenses)

    print(f"\nTotal Spent: ₦{total:,.2f}")

def delete_expense(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        index = int(input("\nEnter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses(expenses)
            print(f"Deleted '{deleted['name']}'.")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
        
def main() -> None:
    expenses = load_expenses()

    while True:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()