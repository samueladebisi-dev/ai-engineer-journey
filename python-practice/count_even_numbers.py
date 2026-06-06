numbers = [2, 5, 8, 11, 14, 17, 20]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even numbers:", count)
