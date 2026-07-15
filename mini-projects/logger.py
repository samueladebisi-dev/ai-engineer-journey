from datetime import datetime


def log(message: str, level: str = "INFO") -> None:
    with open("app.log", "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now()}] [{level}] {message}\n"
        )