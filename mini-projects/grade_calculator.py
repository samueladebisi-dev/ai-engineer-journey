score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
elif score >= 40:
    print("D")
else:
    print("F")
