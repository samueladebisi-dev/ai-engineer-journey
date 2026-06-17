balance = 5000

print("Current Balance:", balance)

amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient funds")

print("Thank you for using our ATM.")
