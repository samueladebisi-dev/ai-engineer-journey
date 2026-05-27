tasks = []

while True:
    task = input("Enter a task (or type quit): ")

    if task.lower() == "quit":
        break

    tasks.append(task)

print("Your Tasks:")
for task in tasks:
    print("-", task)
