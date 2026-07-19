import json
from typing import Any

Expense = dict[str, Any]

def save_json(filename: str, data: list[dict]) -> None:
    """Save Python data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_json(filename: str) -> list[dict]:
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
