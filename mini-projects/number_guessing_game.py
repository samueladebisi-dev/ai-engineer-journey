import random

secret = random.randint(1, 10)

attempts = 3

while attempts > 0:
    guess = int(input("Guess (1-10): "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong!")
        attempts -= 1

print("Game over. Number was:", secret)
