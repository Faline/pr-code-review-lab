import json
from utils import is_empty

def register_user(username, password):
    if is_empty(username) or is_empty(password):
        raise ValueError("Username dan password tidak boleh kosong")

    with open("data/users.json") as f:
        users = json.load(f)

    for user in users:
        if user["username"] == username:
            raise ValueError("Username sudah terdaftar")

    users.append({
        "username": username,
        "password": password
    })

    with open("data/users.json", "w") as f:
        json.dump(users, f)
