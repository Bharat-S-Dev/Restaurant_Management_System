# import json

# with open("menu.json", "r") as file:
#     MENU = json.load(file)

# def remove_items():
#     item_id = input("Enter the Item ID to remove: ").upper()

#     found = False
#     for item in MENU:
#         if item['item_id'] == item_id:
#             MENU.remove(item)
#             found = True
#             break

#     if found:
#         print(f"Item {item_id} removed from the menu.")
#         print("_" * 30)

#         with open("menu.json", "w") as file:
#             json.dump(MENU, file, indent=4)
#             print("Menu updated and saved to file.")
#     else:
#         print("Item ID not found in the menu.")


##########################################

from domain.menu.menu_data import load_menu, save_menu_to_file

def remove_items():
    menu = load_menu()
    item_id = input("Enter the Item ID to remove: ").upper()

    for item in menu:
        if item['item_id'] == item_id:
            menu.remove(item)
            print(f"Item {item_id} removed from the menu.")
            save_menu_to_file(menu)
            return

    print("Item ID not found.")

###############
#########################

# from domain.menu.menu_data import load_menu, save_menu_to_file

# def remove_menu_item():
#     menu = load_menu()
#     item_id = input("Enter item ID to remove: ").upper()

#     updated_menu = [item for item in menu if item["item_id"] != item_id]
#     if len(updated_menu) == len(menu):
#         print("Item not found.")
#     else:
#         save_menu_to_file(updated_menu)
#         print(f"Item {item_id} removed from menu.")
