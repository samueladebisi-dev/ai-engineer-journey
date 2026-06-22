text = input("Enter text: ").lower()

count = 0

for char in text:
    if char in "aeiou":
        count += 1

print("Vowels:", count)
