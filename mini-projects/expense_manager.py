from utils import save_json
from config import DATA_FILE


class ExpenseManager:
    def __init__(self, expenses: list[dict]):
        self.expenses = expenses

    def add(self, expense: dict) -> None:
        self.expenses.append(expense)
        self.save()

    def delete(self, index: int) -> dict:
        deleted = self.expenses.pop(index)
        self.save()
        return deleted

    def all(self) -> list[dict]:
        return self.expenses

    def save(self) -> None:
        save_json(DATA_FILE, self.expenses)