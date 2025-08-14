import json
import os
import pwinput
# import getpass
from database.paths import USERS_FILE


def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# def login():
#     username = input("Enter your username: ").strip()
#     password = pwinput.pwinput(prompt="Enter your password: ", mask="*").strip()
#     users = load_users()

#     if username in users and users[username]["password"] == password:
#         role = users[username]["role"]
#         print("-"*40)
#         print(f"Login successful! Welcome, {username}!")
#         print("-"*40)
#         return username, role
#     else:
#         print("Invalid username or password.")
#         return None, None


def login():
    max_attempts = 3  # Limit attempts
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ").strip()
        password = pwinput.pwinput(prompt="Enter your password: ", mask="*").strip()

        users = load_users()

        if username in users and users[username]["password"] == password:
            print("----------------------------------------")
            print(f"Login successful! Welcome, {username}!")
            print("----------------------------------------")
            return username, users[username]["role"]  # Return role for menu access
        else:
            attempts += 1
            print(f"Invalid username or password. Attempts left: {max_attempts - attempts}")

    print("Too many failed attempts. Returning to main menu.")
    return None, None

