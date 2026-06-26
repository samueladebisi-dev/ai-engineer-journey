import csv

with open("sample.csv", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
