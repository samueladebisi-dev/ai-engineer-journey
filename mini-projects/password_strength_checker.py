password = input("Enter password: ")

if len(password) >= 12:
    print("Strong Password")
elif len(password) >= 8:
    print("Moderate Password")
else:
    print("Weak Password")
