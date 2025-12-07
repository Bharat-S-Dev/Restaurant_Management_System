# from domain.menu.menu_data import load_menu
# from domain.menu.menu_data import MENU

# def display_items(menu_list=None):
#     if menu_list is None:
#         menu_list = load_menu()
        
#     print("\n--- Restaurant Menu ---")
#     categories = []

#     for item in menu_list:
#         if item["category"] not in categories:
#             categories.append(item["category"])

#     for category in categories:
#         print(f"\n----- {category} -----")
#         for item in menu_list:
#             if item["category"] == category:
#                 item_line = f"{item['item_id']} - {item['name']}".ljust(40)
#                 for option, price in item["options"].items():
#                     portions = f"{option.capitalize()}: Rs.{price:.2f}"
#                     print(f"{item_line}{portions}")
#     print("----------------------------")

######################################

# import json
# from domain.menu.menu_data import load_menu

# def display_items(menu_list=MENU):
#     print("\n--- Restaurant Menu ---")
#     categories = list({item["category"] for item in menu_list})

#     for category in categories:
#         print(f"\n----- {category} -----")
#         for item in menu_list:
#             if item["category"] == category:
#                 item_line = f"{item['item_id']} - {item['name']}".ljust(40)
#                 options = ' | '.join([f"{portion.capitalize()}: Rs.{price:.2f}" for portion, price in item['options'].items()])
#                 print(f"{item_line}{options}")
#     print("------------------------")
import json
from domain.menu.menu_data import load_menu

def display_items():
    print("\n--- Restaurant Menu ---")

    menu_list = load_menu()
    if not menu_list:
        print("No menu items found.")
        return

    # Get categories in order of appearance
    categories = []
    for item in menu_list:
        if item["category"] not in categories:
            categories.append(item["category"])

    # Print items grouped by category
    for category in categories:
        print(f"\n----- {category} -----")
        for item in menu_list:
            if item["category"] == category:
                item_line = f"{item['item_id']} - {item['name']}".ljust(40)
                options = " | ".join(
                    [f"{portion.capitalize()}: Rs.{price:.2f}" for portion, price in item["options"].items()]
                )
                print(f"{item_line}{options}")

    print("-"*45)


#######################
##############################
# from domain.menu.menu_data import load_menu

# def display_items():
#     menu = load_menu()
#     if not menu:
#         print("Menu is empty.")
#         return

#     print("\n=== Restaurant Menu ===")
#     for item in menu:
#         print(f"\nItem ID: {item['item_id']}")
#         print(f"Name: {item['name']}")
#         for size, price in item['options'].items():
#             print(f"  {size.title()} - Rs. {price}")
