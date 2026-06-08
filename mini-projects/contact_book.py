contacts = {
    "John": "12345",
    "Sarah": "67890"
}

name = input("Enter contact name: ")
phone = input("Enter phone number: ")

contacts[name] = phone

print(contacts)
print("Total contacts:", len(contacts))
