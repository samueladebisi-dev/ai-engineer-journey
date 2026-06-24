text = input("Enter text: ")

words = len(text.split())
characters = len(text)
sentences = text.count(".") + text.count("!") + text.count("?")

print(f"Words: {words}")
print(f"Characters: {characters}")
print(f"Sentences: {sentences}")
