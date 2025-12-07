import json
from database.paths import ORDERS_FILE
from domain.menu.display_items import display_items
from domain.menu.menu_data import load_menu


menu = load_menu()

# ---------- Load/Save Orders ----------
def load_orders():
    try:
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_orders(orders):
    with open(ORDERS_FILE, "w") as file:
        json.dump(orders, file, indent=4)

# Load current orders from file
current_orders = load_orders()


# ---------- Get Menu Item Details ----------
def get_item_details(item_id):
    """Get full item details from the menu."""
    for item in menu:
        if item['item_id'].upper() == item_id.upper():
            return item
    return None


# ---------- Take Order ----------
def take_order(table_no):
    """Take a new order for a given table."""
    table_no = str(table_no)
    customer_name = input("Enter customer name: ").strip()

    order_items = []
    total_bill = 0.0

    print("\n--- Place Your Order ---")
    display_items()

    while True:
        item_id = input("Enter Item ID (or 'done' to finish): ").strip()
        if item_id.lower() == "done":
            break

        item = get_item_details(item_id)
        if not item:
            print("Invalid Item ID. Try again.")
            continue

        options = list(item['options'].keys())
        if len(options) > 1:
            option = input(f"Choose option ({'/'.join(options)}): ").strip().lower()
            if option not in options:
                print("Invalid option. Try again.")
                continue
        else:
            option = options[0]

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Invalid quantity. Try again.")
            continue

        price = item['options'][option]
        item_total = price * quantity
        order_items.append({
            "item_id": item['item_id'],
            "name": item['name'],
            "portion": option,
            "unit_price": price,
            "quantity": quantity,
            "total_price": item_total
        })
        total_bill += item_total
        print(f"Added {quantity} x {item['name']} ({option}) - Subtotal: Rs.{item_total:.2f}")

    if order_items:
        current_orders[table_no] = {
            "customer": customer_name,
            "items": order_items,
            "total": total_bill
        }
        save_orders(current_orders)
        print(f"\nOrder placed for Table {table_no}. Total: Rs.{total_bill:.2f}")
    else:
        print("No items ordered.")


# ---------- Display Current Orders ----------
def display_current_orders():
    """Show all current orders."""
    if not current_orders:
        print("\nNo active orders.")
        return

    print("\n--- Active Orders ---")
    for table_no, order in current_orders.items():
        print(f"\nTable {table_no} - Customer: {order['customer']}")
        for item in order['items']:
            print(f"  {item['quantity']} x {item['name']} ({item['portion']}) - Rs.{item['total_price']:.2f}")
        print(f"  Total: Rs.{order['total']:.2f}")
    print("---------------------")


# ---------- Cancel Order ----------
def cancel_orders(table_no):
    """Cancel an order for a given table."""
    table_no = str(table_no)
    if table_no not in current_orders:
        print(f"No active order for Table {table_no}.")
        return

    removed_order = current_orders.pop(table_no)
    save_orders(current_orders)
    print(f"Order for Table {table_no} canceled. Refund: Rs.{removed_order['total']:.2f}")


# ---------- Update Order ----------
# def update_order(table_no):
#     """Update quantities in an existing order."""
#     table_no = str(table_no)
#     if table_no not in current_orders:
#         print(f"No order found for Table {table_no}.")
#         return

#     order = current_orders[table_no]

#     while True:
#         print("\n--- Update Order ---")
#         for i, item in enumerate(order['items'], 1):
#             print(f"{i}. {item['quantity']} x {item['name']} ({item['portion']}) - Rs.{item['total_price']:.2f}")

#         try:
#             choice = int(input("Enter item number to update (0 to finish): "))
#         except ValueError:
#             print("Invalid input.")
#             continue

#         if choice == 0:
#             break

#         if 1 <= choice <= len(order['items']):
#             try:
#                 new_qty = int(input("Enter new quantity: "))
#                 if new_qty <= 0:
#                     print("Quantity must be positive.")
#                     continue
#                 item = order['items'][choice - 1]
#                 item['quantity'] = new_qty
#                 item['item_total'] = item['unit_price'] * new_qty
#                 print("Quantity updated.")
#             except ValueError:
#                 print("Invalid number.")
#         else:
#             print("Invalid item number.")

#     order['total'] = sum(item['total_price'] for item in order['items'])
#     save_orders(current_orders)
#     print(f"Order for Table {table_no} updated. New total: Rs.{order['total']:.2f}")

#=================================
def update_order(table_no):
    table_no = str(table_no)

    if table_no not in current_orders:
        print(f"No order found for Table {table_no}.")
        return

    order = current_orders[table_no]

    while True:
        print("\n--- Update Order ---")
        for i in range(len(order["items"])):
            item = order["items"][i]
            print(f"{i+1}. {item['quantity']} x {item['name']} ({item['portion']}) - Rs.{item['total_price']:.2f}")

        choice = input("Enter item number to update (0 to finish): ")

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)
        if choice == 0:
            break
        if choice < 1 or choice > len(order["items"]):
            print("Invalid item number.")
            continue

        item_to_update = order["items"][choice - 1]

        print("\n1. Change quantity")
        print("2. Change item completely")
        print("3. Remove this item")
        print("4. Add new item to order")  # NEW FEATURE
        print("5. Cancel")
        update_choice = input("Choose an option: ")

        if update_choice == "1":
            # Change quantity
            new_qty = input("Enter new quantity: ")
            if not new_qty.isdigit() or int(new_qty) <= 0:
                print("Quantity must be positive.")
                continue
            new_qty = int(new_qty)
            item_to_update["quantity"] = new_qty
            item_to_update["total_price"] = item_to_update["unit_price"] * new_qty
            print(f"Quantity updated. New subtotal: Rs.{item_to_update['total_price']:.2f}")

        elif update_choice == "2":
            # Change entire item
            new_item_id = input("Enter new item ID: ").strip().upper()
            menu_data = load_menu()
            if new_item_id not in menu_data:
                print("Item ID not found in menu.")
                continue

            new_item = menu_data[new_item_id]
            if "Half" in new_item["price"] and "Full" in new_item["price"]:
                portion = input("Choose option (half/full): ").lower()
                if portion not in ["half", "full"]:
                    print("Invalid portion.")
                    continue
                unit_price = new_item["price"][portion.capitalize()]
            else:
                portion = "full"
                unit_price = new_item["price"]["Full"]

            quantity = input("Enter quantity: ")
            if not quantity.isdigit() or int(quantity) <= 0:
                print("Quantity must be positive.")
                continue
            quantity = int(quantity)

            item_to_update["name"] = new_item["name"]
            item_to_update["portion"] = portion
            item_to_update["unit_price"] = unit_price
            item_to_update["quantity"] = quantity
            item_to_update["total_price"] = unit_price * quantity
            print(f"Item changed to {quantity} x {new_item['name']} ({portion}) - Rs.{item_to_update['total_price']:.2f}")

        elif update_choice == "3":
            # Remove item completely
            removed_item = order["items"].pop(choice - 1)
            print(f"Removed {removed_item['name']} from the order.")
            if not order["items"]:
                print("Order is now empty.")
                break

        elif update_choice == "4":
            # Add new item
            menu_data = load_menu()
            new_item_id = input("Enter new item ID: ").strip().upper()
            if new_item_id not in menu_data:
                print("Item ID not found in menu.")
                continue

            new_item = menu_data[new_item_id]
            if "Half" in new_item["price"] and "Full" in new_item["price"]:
                portion = input("Choose option (half/full): ").lower()
                if portion not in ["half", "full"]:
                    print("Invalid portion.")
                    continue
                unit_price = new_item["price"][portion.capitalize()]
            else:
                portion = "full"
                unit_price = new_item["price"]["Full"]

            quantity = input("Enter quantity: ")
            if not quantity.isdigit() or int(quantity) <= 0:
                print("Quantity must be positive.")
                continue
            quantity = int(quantity)

            order["items"].append({
                "name": new_item["name"],
                "portion": portion,
                "unit_price": unit_price,
                "quantity": quantity,
                "total_price": unit_price * quantity
            })
            print(f"Added {quantity} x {new_item['name']} ({portion}) - Rs.{unit_price * quantity:.2f}")

        elif update_choice == "5":
            continue
        else:
            print("Invalid choice.")
            continue

        # Recalculate total
        total_amount = sum(it["total_price"] for it in order["items"])
        order["total"] = total_amount
        print(f"Updated order total: Rs.{order['total']:.2f}")

        more = input("Do you want to update another item? (yes/no): ").lower()
        if more != "yes":
            break

    save_orders(current_orders)
    print(f"Order for Table {table_no} updated successfully.")


if __name__ == "__main__":
    take_order()              # To place a new order
    display_current_orders()  # To see all orders placed
    update_order()
    cancel_orders()
