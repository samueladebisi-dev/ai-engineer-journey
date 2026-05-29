score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

print("Final Score:", score)
