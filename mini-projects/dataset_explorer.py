import csv

filename = input("CSV filename: ")

try:
    with open(filename, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found.")


rows = list(reader)

print(f"Rows: {len(rows)}")

if rows:
    print(f"Columns: {len(rows[0])}")
