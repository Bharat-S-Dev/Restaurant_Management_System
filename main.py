from authentication.auth import register_user, login
from authentication.auth import admin_menu, staff_menu

def main():
    while True:
        print("\n=== Welcome to Restaurant Management System ===")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            register_user()

        elif choice == 2:
            username, role = login()
            if username and role:  
                if role == "admin":
                    admin_menu()
                else:
                    staff_menu()

        elif choice == 3:
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


