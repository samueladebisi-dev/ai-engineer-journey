monthly_saving = float(input("Monthly saving: "))
months = int(input("Number of months: "))

total = monthly_saving * months

print("Total savings:", total)

if total >= 100000:
    print("Great savings habit!")
