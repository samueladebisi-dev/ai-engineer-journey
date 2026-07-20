import csv


def import_expenses(filename: str) -> list[dict]:
    expenses = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

    for row in reader:
        try:
            expenses.append(
                {
                    "name": row["name"],
                    "category": row["category"],
                    "amount": float(row["amount"]),
                }
            )
        except (KeyError, ValueError):
            continue
        
    return expenses