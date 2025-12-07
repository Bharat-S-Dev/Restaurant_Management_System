# import json

# with open("menu.json", "r") as file:
#     MENU = json.load(file)

# def update_items():
#     item_id = input("Enter the Item ID to update: ").upper()

#     for item in MENU:
#         if item['item_id'] == item_id:
#             new_name = input(f"New name (Enter to keep {item['name']}): ")
#             if new_name:
#                 item['name'] = new_name

#             new_cat = input(f"New category (Enter to keep {item['category']}): ")
#             if new_cat:
#                 item['category'] = new_cat.capitalize()

#             print("Current Options:")
#             for size, price in item["options"].items():
#                 print(f"{size.capitalize()}: {price}")

#             if input("Update prices? (y/n): ").lower() == 'y':
#                 new_options = {}
#                 while True:
#                     size = input("Portion size: ").lower()
#                     price = float(input(f"New price for {size}: "))
#                     new_options[size] = price
#                     if input("Add/update more? (y/n): ").lower() != "y":
#                         break
#                 item["options"] = new_options

#             with open("menu.json", "w") as file:
#                 json.dump(MENU, file, indent=4)
#                 print("Item updated and saved.")
#             return

#     print("Item ID not found.")


# ##################################################

# def update_items():
#     item_id = input("Enter the Item ID to update: ").upper()

#     for item in MENU:
#         if item['item_id'] == item_id:
#             print(f"Current Name: {item['name']}")

#             new_name = input("Enter new name (press enter to keep current): ")
#             if new_name:
#                 item['name'] = new_name
#             print(f"Current Category: {item['category']}")

#             new_category = input("Enter new category (press enter to keep current): ")
#             if new_category:
#                 item['category'] = new_category.capitalize()

#             print("Current Options:")
#             for size, price in item['options'].items():
#                 print(f"  {size.capitalize()}: {price}")

#             update_prices = input("Do you want to update prices? (y/n): ").lower()
#             if update_prices == 'y':
#                 new_options = {}
#                 while True:
#                     size = input("Enter portion size (full/half): ").lower()
#                     price = float(input(f"Enter new price for {size}: "))
#                     new_options[size] = price

#                     more = input("Add/update another size? (y/n): ").lower()
#                     if more != 'y':
#                         break
#                 item['options'] = new_options

#             print(f"Item {item_id} updated successfully.")

#             # Save changes to menu.json
#             with open("menu.json", "w") as file:
#                 json.dump(MENU, file, indent=4)
#                 print("Changes saved to menu file.")
#                 print("-" * 40)
#             return

#     print("Item ID not found in the menu.")

    ###############################################
from domain.menu.menu_data import load_menu, save_menu_to_file

def update_items():
    menu = load_menu()
    item_id = input("Enter the Item ID to update: ").upper()

    for item in menu:
        if item['item_id'] == item_id:
            new_name = input("Enter new name (leave blank to keep current): ")
            if new_name:
                item['name'] = new_name

            new_cat = input("Enter new category (leave blank to keep current): ")
            if new_cat:
                item['category'] = new_cat.capitalize()

            if input("Update prices? (y/n): ").lower() == 'y':
                new_options = {}
                while True:
                    size = input("Enter portion size (full/half): ").lower()
                    price = float(input(f"Enter new price for {size}: "))
                    new_options[size] = price
                    if input("Add/update another size? (y/n): ").lower() != 'y':
                        break
                item['options'] = new_options

            print(f"Item {item_id} updated.")
            save_menu_to_file(menu)
            return

    print("Item ID not found.")

# #########################
##################################
# from domain.menu.menu_data import load_menu, save_menu_to_file

# def update_menu_item():
#     menu = load_menu()
#     item_id = input("Enter item ID to update: ").upper()

#     for item in menu:
#         if item["item_id"] == item_id:
#             print(f"Current name: {item['name']}")
#             new_name = input("New name (leave blank to keep): ")
#             if new_name:
#                 item["name"] = new_name

#             try:
#                 new_half = input("New half price (leave blank to keep): ")
#                 if new_half:
#                     item["options"]["half"] = float(new_half)

#                 new_full = input("New full price (leave blank to keep): ")
#                 if new_full:
#                     item["options"]["full"] = float(new_full)

#                 save_menu_to_file(menu)
#                 print("Item updated.")
#                 return
#             except ValueError:
#                 print("Invalid price.")
#                 return

#     print("Item not found.")
