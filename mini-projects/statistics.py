def average(values: list[float]) -> float:
    if not values:
        return 0

    return sum(values) / len(values)

def maximum(values: list[float]) -> float:
    return max(values) if values else 0

def minimum(values: list[float]) -> float:
    return min(values) if values else 0

def total(values: list[float]) -> float:
    return sum(values)

def monthly_total(expenses: list[dict], category: str | None = None) -> float:
    if category:
        filtered = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]
        return sum(expense["amount"] for expense in filtered)

    return sum(expense["amount"] for expense in expenses)

def category_totals(expenses: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = {}

    for expense in expenses:
        category = expense["category"]

        totals[category] = (
            totals.get(category, 0)
            + expense["amount"]
        )

    return totals