text = input("Enter text: ").lower()

vowels = "aeiou"
count = 0

for letter in text:
    if letter in vowels:
        count += 1

print("Vowel count:", count)
