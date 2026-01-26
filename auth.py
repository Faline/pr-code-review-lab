import json

SECRET_KEY = "123456"  # hardcoded secret 😬

def login(username, password):
    with open("data/users.json") as f:
        users = json.load(f)

    for u in users:
        if u["username"] == username and u["password"] == password:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
