contacts = {}

contacts["John"] = "12345"
contacts["Sarah"] = "67890"

name = input("Search contact name: ")

if name in contacts:
    print("Number:", contacts[name])
else:
    print("Not found")

print("Available contacts:")

for contact in contacts:
    print(contact)
