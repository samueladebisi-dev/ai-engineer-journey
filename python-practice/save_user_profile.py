import json

user = {
    "name": "Samuel",
    "goal": "AI Engineer"
}

with open("profile.json", "w") as file:
    json.dump(user, file, indent=4)
