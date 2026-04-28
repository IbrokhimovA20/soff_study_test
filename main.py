import json
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def to_dict(self):
        return {
            "username": self.username,
            "age": self.age
        }

user = User("John", 20)
print(user.to_dict())

with open("users.json", "w") as file:
    json.dump(user.to_dict(), file)