import json
from utils import save_json, load_json
from config import DATA_FILE
import os
from exceptions import InvalidExpenseError

def main() -> None:
    
    
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                expenses = json.load(file)
        else:
            expenses = []
            
        expenses = []

        def display_menu() -> None:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Delete Expense")
            print("4. Exit")
            print("5. Edit Expense")
            print("6. Search Expense")
            
            
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
        def calculate_total(expenses: list[dict]) -> float:
            return sum(expense["amount"] for expense in expenses)
        
        
        print(f"\nTotal Expenses: ₦{calculate_total(expenses):,.2f}")

        total = calculate_total(expenses)
        
        print(f"\nTotal Spent: ₦{total}")


        with open(DATA_FILE, "w") as file:
            json.dump(expenses, file, indent=4)

        category = input("Category: ")


        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        while True:
            display_menu()

            choice = input("Select an option: ")
            
        avg = average(exp["amount"] for exp in expenses)
        print(f"Average Expense: ₦{avg:.2f}")
    
    except InvalidExpenseError as e:
        print(e)

if __name__ == "__main__":
    main()