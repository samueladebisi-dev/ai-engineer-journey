balance = 5000

amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    balance -= amount
    print("Remaining balance:", balance)
else:
    print("Insufficient funds")

print("Thank you for using our ATM.")
