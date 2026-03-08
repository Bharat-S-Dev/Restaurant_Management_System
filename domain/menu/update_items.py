
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


