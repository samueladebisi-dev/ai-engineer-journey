import json

text = '{"name":"Samuel","age":20}'

data = json.loads(text)

print(data)

print(data["name"])