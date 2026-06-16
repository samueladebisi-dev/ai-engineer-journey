weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
obtained = float(input("Marks obtained: "))
total = float(input("Total marks: "))

bmi = weight / (height ** 2)
percentage = (obtained / total) * 100

print("BMI:", round(bmi, 2))
print("Percentage:", round(percentage, 2))
