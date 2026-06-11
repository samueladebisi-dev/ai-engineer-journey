text = input("Enter text: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
