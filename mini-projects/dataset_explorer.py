import csv

filename = input("CSV filename: ")

try:
    with open(filename, newline="") as file:
        rows = list(csv.reader(file))

    print("Columns:")
    print(rows[0])

    print("\nPreview:")

    for row in rows[1:6]:
        print(row)

    print(f"\nRows: {len(rows)-1}")

except FileNotFoundError:
    print("File not found.")
rows = list(reader)

print(f"Rows: {len(rows)}")

if rows:
    print(f"Columns: {len(rows[0])}")
