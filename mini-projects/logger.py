from datetime import datetime

def log(message: str, level: str = "INFO") -> None:
    with open("app.log", "a") as file:
        file.write(
            f"[{datetime.now()}] [{level}] {message}\n"
        )
        
log(f"Deleted expense: {deleted['name']}")        