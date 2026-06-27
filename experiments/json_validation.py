import json

text = '{"name": "Samuel"}'

try:
    json.loads(text)
    print("Valid JSON")
except json.JSONDecodeError:
    print("Invalid JSON")
