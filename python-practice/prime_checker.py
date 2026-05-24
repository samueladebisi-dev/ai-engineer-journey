number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
