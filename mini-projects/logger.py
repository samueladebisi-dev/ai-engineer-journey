from datetime import datetime

def log(message: str) -> None:
    with open("app.log", "a") as file:
        file.write(f"[{datetime.now()}] {message}\n")