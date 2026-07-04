from pathlib import Path

folder = Path(".")

for file in folder.iterdir():
    if file.is_file():
        print(file.name)