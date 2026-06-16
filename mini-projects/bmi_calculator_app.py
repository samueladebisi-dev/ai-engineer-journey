weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))


if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
else:
    print("Overweight")
