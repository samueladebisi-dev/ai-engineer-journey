number = int(input("Enter a number: "))

is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

print("Prime Number" if is_prime else "Not Prime")
