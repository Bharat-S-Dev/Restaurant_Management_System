# import json
# # from domain.menu.menu_data import MENU, save_menu_to_file

# with open("menu.json", "r") as file:
#     MENU = json.load(file)

# def add_menu():
#     item_id = input("Enter new item ID: ").upper()

#     if any(item['item_id'] == item_id for item in MENU):
#         print("Item ID already exists.")
#         return

#     name = input("Enter item name: ").capitalize()
#     category = input("Enter category(Breakfast/Lunch...): ").capitalize()
#     options = {}

#     while True:
#         size = input("Enter portion size (full/half): ").lower()
#         price = float(input(f"Enter price for {size}: "))
#         options[size] = price

#         if input("Add another size? (y/n): ").lower() != "y":
#             break

#     new_item = {
#         "item_id": item_id,
#         "name": name,
#         "category": category,
#         "options": options
#     }

#     MENU.append(new_item)
#     print(f"{name} added to the menu under {category}.")

#     with open("menu.json", "w") as file:
#         json.dump(MENU, file, indent=4)
#         print("Menu updated and saved.")
###############################

# import json
# from domain.menu.menu_data import MENU, save_menu_to_file

# def add_menu():
#     item_id = input("Enter new item ID: ").upper()
#     if any(item['item_id'] == item_id for item in MENU):
#         print("Item ID already exists.")
#         return
    
#     name = input("Enter item Name: ").capitalize()
#     category = input("Enter Category (Breakfast/Lunch...): ").capitalize()
#     options = {}
#     while True:
#         size = input("Enter portion size (full/half): ").lower()
#         price = float(input(f"Enter price for {size}: "))
#         options[size] = price
#         if input("Add another size? (y/n): ").lower() != 'y':
#             break

#     MENU.append({
#         "item_id": item_id,
#         "name": name,
#         "category": category,
#         "options": options
#     })
#     print(f"{name} added to the menu under {category}.")
#     save_menu_to_file()

# #################################################
from domain.menu.menu_data import load_menu, save_menu_to_file

def add_menu():
    menu = load_menu()

    item_id = input("Enter new item ID: ").upper()
    if any(item['item_id'] == item_id for item in menu):
        print("Item ID already exists.")
        return

    name = input("Enter item Name: ").capitalize()
    category = input("Enter Category (Breakfast/Lunch/etc): ").capitalize()

    options = {}
    while True:
        size = input("Enter portion size (full/half): ").lower()
        price = float(input(f"Enter price for {size}: "))
        options[size] = price

        add_more = input("Add another size? (y/n): ").lower()
        if add_more != "y":
            break

    new_item = {
        "item_id": item_id,
        "name": name,
        "category": category,
        "options": options
    }

    menu.append(new_item)
    save_menu_to_file(menu)

    print("-" * 40)
    print(f"{name} added to the menu under {category}.")
    print("Menu updated and saved to file.")
    print("-" * 40)


################################################
########################3
# from domain.menu.menu_data import load_menu, save_menu_to_file

# def add_menu_item():
#     menu = load_menu()

#     item_id = input("Enter item ID: ").upper()
#     for item in menu:
#         if item['item_id'] == item_id:
#             print("Item ID already exists.")
#             return

#     name = input("Enter item name: ")
#     half_price = float(input("Enter price for half: "))
#     full_price = float(input("Enter price for full: "))

#     new_item = {
#         "item_id": item_id,
#         "name": name,
#         "options": {
#             "half": half_price,
#             "full": full_price
#         }
#     }

#     menu.append(new_item)
#     save_menu_to_file(menu)
#     print(f"{name} added to menu.")
