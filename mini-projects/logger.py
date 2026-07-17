from datetime import datetime


def log(message: str, level: str = "INFO") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(
        "app.log",
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            f"[{timestamp}] [{level}] {message}\n"
        )