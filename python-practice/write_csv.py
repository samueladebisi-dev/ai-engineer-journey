import csv

rows = [
    ["Name", "Score"],
    ["Samuel", 92],
    ["Grace", 88]
]

with open("scores.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV created.")
