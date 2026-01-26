from auth import login
from user_service import register_user

def get_user_action():
    import sys
    while True:
        action = input("login/register: ")
        if action in ('login', 'register', 'quit'):
            return action
        print('unknown action')

def main():
    print("Welcome to User System")

    action = get_user_action()

    if action == "login":
        u = input("username: ")
        p = input("password: ")
        print(login(u, p))
    if action == "register":
        u = input("username: ")
        p = input("password: ")
        register_user(u, p)
        print("user created")
    if action == 'quit':
        print('exit system')

if __name__ == "__main__":
    main()
