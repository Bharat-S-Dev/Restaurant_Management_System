# import json
# import os

# # MENU_FILE = "menu.json"
# MENU_FILE = "database/menu.json"

# def load_menu():
#     if os.path.exists(MENU_FILE):
#         with open(MENU_FILE, "r") as file:
#             return json.load(file)
#     return []


# def save_menu_to_file(menu):
#     with open(MENU_FILE, "w") as file:
#         json.dump(menu, file, indent=4)


# import json
# import os
# from database.paths import MENU_FILE

# MENU = []

# def load_menu_from_file():
#     global MENU
#     if os.path.exists(MENU_FILE):
#         with open(MENU_FILE, 'r') as f:
#             MENU = json.load(f)
#     else:
#         MENU = []

# def save_menu_to_file():
#     with open(MENU_FILE, 'w') as f:
#         json.dump(MENU, f, indent=4)

# # Load on import
# load_menu_from_file()


# domain/menu/menu_data.py

import json
import os
from database.paths import MENU_FILE

def load_menu():
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r') as file:
            return json.load(file)
    return []

def save_menu_to_file(menu_data):
    with open(MENU_FILE, 'w') as file:
        json.dump(menu_data, file, indent=2)




