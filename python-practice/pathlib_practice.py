from pathlib import Path

current = Path.cwd()

print("Current directory:")
print(current)

print("\nPython files:")

for file in current.glob("*.py"):
    print(file.name)