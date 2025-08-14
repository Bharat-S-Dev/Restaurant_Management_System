from authentication.login import login
from authentication.register import register_user

# Staff features
from domain.orders import take_order, update_order, cancel_orders, display_current_orders
from domain.tables import reserve_table, free_table, view_tables
from domain.billing import generate_bill

# Admin features
from domain.menu.menu_data import load_menu, save_menu_to_file
from domain.menu.add_items import  add_menu
from domain.menu.update_items import update_items
from domain.menu.remove_items import remove_items
from domain.menu.display_items import display_items
# from domain.reports import show_all_bills, show_daily_sales
from domain.reports import generate_report

def main():
    while True:
        print("\n=== Welcome to Restaurant Management System ===")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            role = login()
            if role == "admin":
                admin_menu()
            elif role == "staff":
                staff_menu()
        elif choice == "3":
            print("Thank you. Exiting.")
            break
        else:
            print("Invalid choice.")


# ----------------- Admin Menu -----------------

def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("-"*25)
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Update Menu Item")
        print("4. Remove Menu Item")
        print("5. Reports")
        print("6. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_items()
        elif choice == "2":
            add_menu()
        elif choice == "3":
            update_items()
        elif choice == "4":
            remove_items()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Logging out.")
            break
        else:
            print("Invalid choice.Try again.")


# ----------------- Staff Menu -----------------

def staff_menu():
    while True:
        print("\n=== Staff Menu ===")
        print("-"*25)
        print("1. Reserve Table")
        print("2. Free Table")
        print("3. View Table Status")
        print("4. Take New Order")
        print("5. Update Order")
        print("6. Cancel Order")
        print("7. Display Active Orders")
        print("8. Generate Bill")
        print("9. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            table = input("Enter table number: ")
            reserve_table(table)
        elif choice == 2:
            table = input("Enter table number: ")
            free_table(table)
        elif choice == 3:
            view_tables()
        elif choice == 4:
            table_no = input("Enter table number: ")
            take_order(table_no)
        elif choice == 5:
            table_no = input("Enter table number: ")
            update_order(table_no)
        elif choice == 6:
            table_no = input("Enter table number: ")
            cancel_orders(table_no)
        elif choice == 7:
            display_current_orders()
        elif choice == 8:
            table_no = input("Enter table number: ")
            generate_bill(table_no)
        elif choice == 9:
            print("Logging out.")
            break
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()