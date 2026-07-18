import json
from logger import log
from config import DATA_FILE
from exceptions import InvalidExpenseError
import os
from statistics import (
    average,
    maximum,
    minimum,
    total as total_amount,
    monthly_total,
    category_totals,
)
from csv_export import export_expenses
from csv_import import import_expenses

def display_menu() -> None:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search by Category")
    print("5. Edit Expense")
    print("6. Sort by Amount")
    print("7. Sort by Name")
    print("8. Export to CSV")
    print("9. Import from CSV")
    print("10. Exit")


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
    
    amounts = [expense["amount"] for expense in expenses]

    total = total_amount(amounts)
    
    amounts = [expense["amount"] for expense in expenses]
    
    highest = maximum(amounts)
    lowest = minimum(amounts)
    avg = average(amounts)
    monthly = monthly_total(expenses)


    print(f"Lowest Expense: ₦{lowest:,.2f}")
    print(f"Highest Expense: ₦{highest:,.2f}")
    print(f"Average Expense: ₦{avg:,.2f}")
    print(f"Monthly Total: ₦{monthly:,.2f}")
    print(f"\nTotal Spent: ₦{total:,.2f}")
    print("\nCategory Summary")

    for category, amount in category_totals(expenses).items():
        print(f"- {category}: ₦{amount:,.2f}")
    
    
def sort_by_amount(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses found.")
        return

    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense["amount"]
    )

    for index, expense in enumerate(sorted_expenses, start=1):
        print(f"{index}. ", end="")
        display_expense(expense)

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
            log(f"Deleted expense: {deleted['name']}")
            print(f"Deleted '{deleted['name']}'.")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
        return
    
def search_by_category(expenses: list[dict]) -> None:
    category = input("Category: ").strip().lower()

    results = [
        expense for expense in expenses
        if expense["category"].lower() == category
    ]

    if not results:
        print("No matching expenses.")
        return

    for index, expense in enumerate(results, start=1):
        print(f"{index}. ", end="")
        display_expense(expense)
        
def edit_expense(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses available.")
        return

    view_expenses(expenses)

    try:
        index = int(input("\nEnter expense number to edit: ")) - 1

        if not 0 <= index < len(expenses):
            print("Invalid expense number.")
            return

        expense = expenses[index]

        expense["name"] = input(
            f"Name ({expense['name']}): "
        ) or expense["name"]

        expense["category"] = input(
            f"Category ({expense['category']}): "
        ) or expense["category"]

        amount = input(
            f"Amount ({expense['amount']}): "
        )

        if amount:
            expense["amount"] = float(amount)

        save_expenses(expenses)

        print("Expense updated successfully.")

    except ValueError:
        print("Invalid input.")
        
def sort_by_amount(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses found.")
        return

    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense["amount"]
    )

    for index, expense in enumerate(sorted_expenses, start=1):
        print(f"{index}. ", end="")
        display_expense(expense)

def sort_by_name(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses available.")
        return

    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense["name"].lower()
    )

    print("\nExpenses (A-Z)\n")

    for index, expense in enumerate(sorted_expenses, start=1):
        print(f"{index}. ", end="")
        display_expense(expense)

def export_to_csv(expenses: list[dict]) -> None:
    filename = input("Enter export filename: ").strip()

    if not filename.endswith(".csv"):
        filename += ".csv"

    export_expenses(expenses, filename)
    log(f"Exported expenses to {filename}")                               
    print(f"Expenses exported to {filename}")

def import_from_csv(expenses: list[dict]) -> None:
    filename = input("CSV filename: ").strip()

    imported = import_expenses(filename)

    expenses.extend(imported)

    save_expenses(expenses)

    log(f"Imported {len(imported)} expenses from {filename}")

    print(f"Imported {len(imported)} expenses.")
    
    existing = {
        (e["name"], e["category"], e["amount"])
        for e in expenses
    }

    for expense in imported:
        key = (
            expense["name"],
            expense["category"],
            expense["amount"],
        )

        if key not in existing:
            expenses.append(expense)
      
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
            search_by_category(expenses)
            
        elif choice == "5":
            edit_expense(expenses)

        elif choice == "6":
            sort_by_amount(expenses)
            
        elif choice == "7":
            sort_by_name(expenses)
            print("Expenses sorted by name.")
            
        elif choice == "8":
            export_to_csv(expenses)
        
        elif choice == "9":
            import_from_csv(expenses)
        
        elif choice == "10":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()