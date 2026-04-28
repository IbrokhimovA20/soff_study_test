import json

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)