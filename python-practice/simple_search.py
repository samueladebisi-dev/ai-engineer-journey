items = ["python", "ai", "github", "machine learning"]

query = input("Search: ").lower()

if query in items:
    print("Found:", query)
else:
    print("Not found")
