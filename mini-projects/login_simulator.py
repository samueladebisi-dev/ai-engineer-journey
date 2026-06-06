username = "admin"
password = "1234"

attempts = 3

while attempts > 0:
    user = input("Username: ")
    pwd = input("Password: ")

    if user == username and pwd == password:
        print("Login successful")
        break

    attempts -= 1
    print("Access denied")

if attempts == 0:
    print("No attempts remaining")
