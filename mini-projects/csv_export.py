import csv


def export_expenses(expenses: list[dict], filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "category", "amount"]
        )

        writer.writeheader()
        writer.writerows(expenses)