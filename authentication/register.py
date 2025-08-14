import json
import os
import pwinput
from database.paths import USERS_FILE

# USER_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def register_user():
    users = load_users()

    while True:
        username = input("Enter a new username: ")
        if username.lower() == "madhav":
            print("You cannot register as admin.")
            continue

        if username in users:
            print("Username already exists. Please choose a different one.")
        else:
            password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
            role = "staff"
            users[username] = {"password": password, "role": role}
            save_users(users)
            print(f"Registration successful! You are registered as {role}.")
            return role


