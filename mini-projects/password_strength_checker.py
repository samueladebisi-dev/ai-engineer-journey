password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

print("Strength Score:", score, "/3")
