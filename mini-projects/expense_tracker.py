expenses = []

while True:
    amount = input("Enter expense (or quit): ")

    if amount.lower() == "quit":
        break

    expenses.append(float(amount))
    
print("Total Expenses:", sum(expenses))
print("Number of Entries:", len(expenses))


average = sum(expenses) / len(expenses)

print("Average Expense:", average)

print("4. Delete Expense")


elif choice == "4":
    if not expenses:
        print("No expenses to delete.")
        continue

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - ₦{expense['amount']}")

    delete_index = int(input("Enter expense number: ")) - 1

    if 0 <= delete_index < len(expenses):
        expenses.pop(delete_index)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense deleted.")
    else:
        print("Invalid selection.")
        
category = input("Category: ")

expenses.append({
    "name": name,
    "amount": amount,
    "category": category
})


for expense in expenses:
    print(
        f"{expense['name']} | {expense['category']} | ₦{expense['amount']}"
    )
    
print("5. Edit Expense")


elif choice == "5":
    if not expenses:
        print("No expenses available.")
        continue

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - ₦{expense['amount']}")

    edit_index = int(input("Select expense: ")) - 1

    if 0 <= edit_index < len(expenses):
        expenses[edit_index]["name"] = input("New name: ")
        expenses[edit_index]["amount"] = float(input("New amount: "))
        expenses[edit_index]["category"] = input("New category: ")

        save_json("expenses.json", expenses)

        print("Expense updated successfully.")