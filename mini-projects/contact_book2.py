contacts = {}

while True:
    name = input("Enter contact name (or quit): ")

    if name.lower() == "quit":
        break

    phone = input("Enter phone number: ")

    contacts[name] = phone

print("\nContacts:")

for name, phone in contacts.items():
    print(name, "-", phone)
