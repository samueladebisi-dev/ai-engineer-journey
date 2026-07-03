import json
from typing import Any

def save_json(filename: str, data: list[Any]) -> None:
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_json(filename: str) -> list:
    with open(filename, "r") as file:
        return json.load(file)
