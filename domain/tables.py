# import random

# tables = []

# for i in range(10):
#     occupancy_options = [2, 4, 8]
#     random_occupancy = random.choice(occupancy_options)
#     table = {
#         'table_no': i + 1,
#         'status': 'Available',
#         'occupancy': random_occupancy
#     }
#     tables.append(table)

# def display_available_tables(table_list):
#     print("\n--- Available Tables ---")

#     available_found = False
#     for table in table_list:
#         if table['status'] == 'Available':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Status: {table['status']}")
#             available_found = True
#     if not available_found:
#         print("No tables currently available.")
#     print("------------------------")

# def reserve_table(table_list, table_number):

#     for table in table_list:
#         if table['table_no'] == table_number:
#             if table['status'] == 'Available':
#                 table['status'] = 'Reserved'
#                 print(f"Table {table_number} has been reserved.")
#                 return True
#             else:
#                 print(f"Table {table_number} is already {table['status']}.")
#                 return False
#     print(f"Table {table_number} not found.")
#     return False

# # --- Main Program Logic ---
# while True:
#     print("\n--- Restaurant Management ---")
#     print("1. View Available Tables")
#     print("2. Reserve a Table")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         display_available_tables(tables)
#     elif choice == '2':
#         try:
#             table_to_reserve = int(input("Enter the table number to reserve: "))
#             reserve_table(tables, table_to_reserve)
#         except ValueError:
#             print("Invalid input. Please enter a valid table number.")  #
#     elif choice == '3':
#         print("Exiting restaurant management system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


# #--------------------------3rd/updated--------------------

# tables = [
#     {'table_no': 1, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 2, 'status': 'Available', 'occupancy': 2},
#     {'table_no': 3, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 4, 'status': 'Available', 'occupancy': 8},
#     {'table_no': 5, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 6, 'status': 'Available', 'occupancy': 2},
#     {'table_no': 7, 'status': 'Available', 'occupancy': 6},
#     {'table_no': 8, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 9, 'status': 'Available', 'occupancy': 8},
#     {'table_no': 10, 'status': 'Available', 'occupancy': 2}
# ]

# def display_available_tables(table_list):
#
#     print("\n--- Available Tables ---")
#     available_found = False
#     for table in table_list:
#         if table['status'] == 'Available':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Status: {table['status']}")
#             available_found = True
#     if not available_found:
#         print("No tables currently available.")
#     print("------------------------")

# def reserve_multiple_tables(table_list, table_numbers_str):
#
#     # Split the input string by commas or spaces and convert to integers
#     table_numbers_to_reserve = []
#     try:
#         raw_numbers = table_numbers_str.replace(',', ' ').split()
#         for num_str in raw_numbers:
#             table_numbers_to_reserve.append(int(num_str))
#     except ValueError:
#         print("Invalid input. Please enter valid table numbers separated by spaces or commas.")
#         return

#     reserved_count = 0
#     for table_number in table_numbers_to_reserve:
#         found_table = False
#         for table in table_list:
#             if table['table_no'] == table_number:
#                 found_table = True
#                 if table['status'] == 'Available':
#                     table['status'] = 'Reserved'
#                     print(f"Table {table_number} has been reserved.")
#                     reserved_count += 1
#                 else:
#                     print(f"Table {table_number} is already {table['status']}.")
#                 break
#         if not found_table:
#             print(f"Table {table_number} not found.")
    
#     if reserved_count > 0:
#         print(f"\n{reserved_count} table(s) successfully reserved.")
#     else:
#         print("\nNo tables were reserved.")


# # --- Main Program Logic ---
# while True:
#     print("\n--- Restaurant Management ---")
#     print("1. View Available Tables")
#     print("2. Reserve Table(s)")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         display_available_tables(tables)
#     elif choice == '2':
#         table_to_reserve_input = input("Enter the table number(s) to reserve (e.g., 2, 5, 7 or 2 5 7): ")
#         reserve_multiple_tables(tables, table_to_reserve_input)
#     elif choice == '3':
#         print("Exiting restaurant management system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

#--------------------------

# tables_data = [
#     {'table_no': 1, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 2, 'status': 'Available', 'occupancy': 2},
#     {'table_no': 3, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 4, 'status': 'Available', 'occupancy': 8},
#     {'table_no': 5, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 6, 'status': 'Available', 'occupancy': 2},
#     {'table_no': 7, 'status': 'Available', 'occupancy': 6},
#     {'table_no': 8, 'status': 'Available', 'occupancy': 4},
#     {'table_no': 9, 'status': 'Available', 'occupancy': 8},
#     {'table_no': 10, 'status': 'Available', 'occupancy': 2}
# ]

# def display_available_tables(table_list):
#     print("\n--- Available Tables ---")

#     available_found = False

#     for table in table_list:
#         if table['status'] == 'Available':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Status: {table['status']}")

#             available_found = True

#     if not available_found:
#         print("No tables currently available.")
#     print("------------------------------------")


# def find_suitable_tables(table_list, num_people):
  
#     suitable_tables = []

#     for table in table_list:
#         if table['status'] == 'Available' and table['occupancy'] >= num_people:
#             suitable_tables.append(table)
#     return suitable_tables


# def reserve_multiple_tables(table_list, table_numbers_str, num_people):

#     table_numbers_to_reserve = []

#     try:
#         raw_numbers = table_numbers_str.replace(',', ' ').split()
#         for num_str in raw_numbers:
#             table_numbers_to_reserve.append(int(num_str))
#     except ValueError:
#         print("Invalid input. Please enter valid table numbers separated by spaces or commas.")
#         return

#     reserved_count = 0

#     for table_number in table_numbers_to_reserve:
#         found_table = False
#         for table in table_list:
#             if table['table_no'] == table_number:
#                 found_table = True
#                 if table['status'] == 'Available':
#                     if table['occupancy'] >= num_people:
#                         table['status'] = 'Reserved'
#                         print(f"Table {table_number} has been reserved for {num_people} people.")
#                         reserved_count += 1
#                     else:
#                         print(f"Table {table_number} ({table['occupancy']} seater) is too small for {num_people} people.")
#                 else:
#                     print(f"Table {table_number} is already {table['status']}.")
#                 break
#         if not found_table:
#             print(f"Table {table_number} not found.")
    
#     if reserved_count > 0:
#         print(f"\n{reserved_count} table(s) successfully reserved.")
#     else:
#         print("\nNo tables were reserved.")


# # --- Main Program Logic ---
# while True:
#     print("\n--- Restaurant Management ---")
#     print("1. View Available Tables")
#     print("2. Reserve Table(s)")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         display_available_tables(tables_data)
#     elif choice == '2':
#         try:
#             num_people_input = int(input("How many people are in your party? ")) # Ask for the number of people
#             if num_people_input <= 0:
#                 print("Number of people must be at least 1.")
#                 continue

#             suitable_tables = find_suitable_tables(tables_data, num_people_input)
#             if suitable_tables:
#                 print("\nAvailable tables that can accommodate your party:")
#                 for table in suitable_tables:
#                     print(f"Table {table['table_no']} ({table['occupancy']} seater)")
                
#                 table_to_reserve_input = input("Enter the table number(s) to reserve (e.g., 2, 5, 7): ")
#                 reserve_multiple_tables(tables_data, table_to_reserve_input, num_people_input)
#             else:
#                 print("No available tables can accommodate your party size.")

#         except ValueError:
#             print("Invalid input. Please enter a valid number.") #
#     elif choice == '3':
#         print("Exiting restaurant management system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

#=====================================================================================

# import json
# import os

# # === Load and Save from JSON ===

# TABLES_FILE = "tables.json"

# def load_tables_from_file():
#     if os.path.exists(TABLES_FILE):
#         with open(TABLES_FILE, "r") as file:
#             return json.load(file)
#     else:
#         # Default tables
#         return [
#             {'table_no': 1, 'status': 'Available', 'occupancy': 4},
#             {'table_no': 2, 'status': 'Available', 'occupancy': 2},
#             {'table_no': 3, 'status': 'Available', 'occupancy': 4},
#             {'table_no': 4, 'status': 'Available', 'occupancy': 8},
#             {'table_no': 5, 'status': 'Available', 'occupancy': 4},
#             {'table_no': 6, 'status': 'Available', 'occupancy': 2},
#             {'table_no': 7, 'status': 'Available', 'occupancy': 6},
#             {'table_no': 8, 'status': 'Available', 'occupancy': 4},
#             {'table_no': 9, 'status': 'Available', 'occupancy': 8},
#             {'table_no': 10, 'status': 'Available', 'occupancy': 2}
#         ]

# def save_tables_to_file(table_list):
#     with open(TABLES_FILE, "w") as file:
#         json.dump(table_list, file, indent=4)


# def display_available_tables(table_list):
#     print("\n--- Available Tables ---")

#     available_found = False

#     for table in table_list:
#         if table['status'] == 'Available':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Status: {table['status']}")
#             available_found = True

#     if not available_found:
#         print("No tables currently available.")
#     print("------------------------------------")


# def find_suitable_tables(table_list, num_people):
#     suitable_tables = []

#     for table in table_list:
#         if table['status'] == 'Available' and table['occupancy'] >= num_people:
#             suitable_tables.append(table)
#     return suitable_tables


# def reserve_multiple_tables(table_list, table_numbers_str, num_people):

#     table_numbers_to_reserve = []

#     try:
#         raw_numbers = table_numbers_str.replace(',', ' ').split()
#         for num_str in raw_numbers:
#             table_numbers_to_reserve.append(int(num_str))
#     except ValueError:
#         print("Invalid input. Please enter valid table numbers separated by spaces or commas.")
#         return

#     reserved_count = 0

#     for table_number in table_numbers_to_reserve:
#         found_table = False
#         for table in table_list:
#             if table['table_no'] == table_number:
#                 found_table = True
#                 if table['status'] == 'Available':
#                     if table['occupancy'] >= num_people:
#                         table['status'] = 'Reserved'
#                         print(f"Table {table_number} has been reserved for {num_people} people.")
#                         reserved_count += 1
#                     else:
#                         print(f"Table {table_number} ({table['occupancy']} seater) is too small for {num_people} people.")
#                 else:
#                     print(f"Table {table_number} is already {table['status']}.")
#                 break
#         if not found_table:
#             print(f"Table {table_number} not found.")

#     if reserved_count > 0:
#         save_tables_to_file(table_list)
#         print(f"\n{reserved_count} table(s) successfully reserved.")
#     else:
#         print("\nNo tables were reserved.")


# def cancel_booking(table_list):
#     try:
#         table_no = int(input("Enter the table number to cancel booking: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         return

#     for table in table_list:
#         if table['table_no'] == table_no:
#             if table['status'] == 'Reserved':
#                 table['status'] = 'Available'
#                 save_tables_to_file(table_list)
#                 print(f"Table {table_no} booking has been canceled.")
#                 return
#             else:
#                 print(f"Table {table_no} is not currently reserved.")
#                 return
#     print("Table not found.")


# # --- Main Program Logic ---
# tables_data = load_tables_from_file()

# while True:
#     print("\n--- Restaurant Management ---")
#     print("1. View Available Tables")
#     print("2. Reserve Table(s)")
#     print("3. Cancel Table Booking")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         display_available_tables(tables_data)
#     elif choice == '2':
#         try:
#             num_people_input = int(input("How many people are in your party? "))
#             if num_people_input <= 0:
#                 print("Number of people must be at least 1.")
#                 continue

#             suitable_tables = find_suitable_tables(tables_data, num_people_input)
#             if suitable_tables:
#                 print("\nAvailable tables that can accommodate your party:")
#                 for table in suitable_tables:
#                     print(f"Table {table['table_no']} ({table['occupancy']} seater)")

#                 table_to_reserve_input = input("Enter the table number(s) to reserve (e.g., 2, 5, 7): ")
#                 reserve_multiple_tables(tables_data, table_to_reserve_input, num_people_input)
#             else:
#                 print("No available tables can accommodate your party size.")

#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#     elif choice == '3':
#         cancel_booking(tables_data)
#     elif choice == '4':
#         print("Exiting restaurant management system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

#===============================================================================


# import json
# import os
# from itertools import combinations

# # === Load and Save from JSON ===

# TABLES_FILE = "tables.json"


# def load_tables_from_file():
#     if os.path.exists(TABLES_FILE):
#         with open(TABLES_FILE, "r") as file:
#             return json.load(file)
#     else:
#         return [
#             {'table_no': 1, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 2, 'status': 'Available', 'occupancy': 2, 'reserved_for': None},
#             {'table_no': 3, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 4, 'status': 'Available', 'occupancy': 8, 'reserved_for': None},
#             {'table_no': 5, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 6, 'status': 'Available', 'occupancy': 2, 'reserved_for': None},
#             {'table_no': 7, 'status': 'Available', 'occupancy': 6, 'reserved_for': None},
#             {'table_no': 8, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 9, 'status': 'Available', 'occupancy': 8, 'reserved_for': None},
#             {'table_no': 10, 'status': 'Available', 'occupancy': 2, 'reserved_for': None}
#         ]


# def save_tables_to_file(table_list):
#     with open(TABLES_FILE, "w") as file:
#         json.dump(table_list, file, indent=4)


# def display_available_tables(table_list):
#     print("\n--- Available Tables ---")
#     available_found = False
#     for table in table_list:
#         if table['status'] == 'Available':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Status: {table['status']}")
#             available_found = True
#     if not available_found:
#         print("No tables currently available.")
#     print("------------------------------------")


# def display_reserved_tables(table_list):
#     print("\n--- Reserved Tables ---")

#     found = False

#     for table in table_list:
#         if table['status'] == 'Reserved':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Reserved for {table['status']} people")
            
#             found = True

#     if not found:
#         print("No tables currently reserved.")
#     print("------------------------------------")


# def find_combination_to_fit(table_list, num_people):
#     available_tables = [t for t in table_list if t['status'] == 'Available']
#     for r in range(1, len(available_tables) + 1):
#         for combo in combinations(available_tables, r):
#             total_capacity = sum(t['occupancy'] for t in combo)
#             if total_capacity >= num_people:
#                 return combo
#     return []


# def reserve_tables_automatically(table_list, num_people):
#     selected_tables = find_combination_to_fit(table_list, num_people)

#     if not selected_tables:
#         print("No available table combination can accommodate your party size.")
#         return

#     for table in selected_tables:
#         table['status'] = 'Reserved'
#         table['reserved_for'] = num_people
#         print(f"Table {table['table_no']} ({table['occupancy']} seater) reserved.")
#     save_tables_to_file(table_list)
#     print(f"\n{len(selected_tables)} table(s) reserved for {num_people} people.")


# def cancel_booking(table_list):
#     try:
#         table_no = int(input("Enter the table number to cancel booking: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         return

#     for table in table_list:
#         if table['table_no'] == table_no:
#             if table['status'] == 'Reserved':
#                 table['status'] = 'Available'
#                 table['reserved_for'] = None
#                 save_tables_to_file(table_list)
#                 print(f"Table {table_no} booking has been canceled.")
#                 return
#             else:
#                 print(f"Table {table_no} is not currently reserved.")
#                 return
#     print("Table not found.")


# # --- Main Program Logic ---
# tables_data = load_tables_from_file()

# while True:
#     print("\n--- Restaurant Management ---")
#     print("1. View Available Tables")
#     print("2. Reserve Table(s)")
#     print("3. Cancel Table Booking")
#     print("4. View Reserved Tables")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         display_available_tables(tables_data)

#     elif choice == '2':
#         try:
#             num_people_input = int(input("How many people are in your party? "))
#             if num_people_input <= 0:
#                 print("Number of people must be at least 1.")
#                 continue
#             reserve_tables_automatically(tables_data, num_people_input)
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

#     elif choice == '3':
#         cancel_booking(tables_data)

#     elif choice == '4':
#         display_reserved_tables(tables_data)

#     elif choice == '5':
#         print("Exiting restaurant management system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


###########################################################################


# import json
# import os
# from itertools import combinations
# from datetime import datetime

# # === Load and Save from JSON ===

# TABLES_FILE = "database/tables.json"


# def load_tables_from_file():
#     if os.path.exists(TABLES_FILE):
#         with open(TABLES_FILE, "r") as file:
#             return json.load(file)
#     else:
#         return [
#             {'table_no': 1, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 2, 'status': 'Available', 'occupancy': 2, 'reserved_for': None},
#             {'table_no': 3, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 4, 'status': 'Available', 'occupancy': 8, 'reserved_for': None},
#             {'table_no': 5, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 6, 'status': 'Available', 'occupancy': 2, 'reserved_for': None},
#             {'table_no': 7, 'status': 'Available', 'occupancy': 6, 'reserved_for': None},
#             {'table_no': 8, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#             {'table_no': 9, 'status': 'Available', 'occupancy': 8, 'reserved_for': None},
#             {'table_no': 10, 'status': 'Available', 'occupancy': 2, 'reserved_for': None}
#         ]


# def save_tables_to_file(table_list):
#     with open(TABLES_FILE, "w") as file:
#         json.dump(table_list, file, indent=4)


# def display_available_tables(table_list):
#     print("\n--- Available Tables ---")
#     available_found = False
#     for table in table_list:
#         if table['status'] == 'Available':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Status: {table['status']}")
#             available_found = True
#     if not available_found:
#         print("No tables currently available.")
#     print("------------------------------------")


# def display_reserved_tables(table_list):
#     print("\n--- Reserved Tables ---")

#     found = False

#     for table in table_list:
#         if table['status'] == 'Reserved':
#             print(f"Table {table['table_no']} ({table['occupancy']} seater) - Reserved for {table['reserved_for']} people on {table.get('reservation_date', 'N/A')} at {table.get('reservation_time', 'N/A')}")
#             found = True

#     if not found:
#         print("No tables currently reserved.")
#     print("------------------------------------")


# def find_combination_to_fit(table_list, num_people):
#     available_tables = [t for t in table_list if t['status'] == 'Available']
#     for r in range(1, len(available_tables) + 1):
#         for combo in combinations(available_tables, r):
#             total_capacity = sum(t['occupancy'] for t in combo)
#             if total_capacity >= num_people:
#                 return combo
#     return []


# def reserve_tables_automatically(table_list, num_people):
#     selected_tables = find_combination_to_fit(table_list, num_people)

#     if not selected_tables:
#         print("No available table combination can accommodate your party size.")
#         return
    
#     # Ask and validate date
#     while True:
#         reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
#         try:
#             datetime.strptime(reservation_date, "%Y-%m-%d")
#             break
#         except ValueError:
#             print("Invalid date format. Please use YYYY-MM-DD.")

#     reservation_time = input("Enter reservation time (e.g. 7:00 PM): ")


#     for table in selected_tables:
#         table['status'] = 'Reserved'
#         table['reserved_for'] = num_people
#         table['reservation_date'] = reservation_date
#         table['reservation_time'] = reservation_time
#         print(f"Table {table['table_no']} ({table['occupancy']} seater) reserved.")

#     save_tables_to_file(table_list)
#     print(f"\n{len(selected_tables)} table(s) reserved for {num_people} people on {reservation_date} at {reservation_time}.")


# def cancel_booking(table_list):
#     try:
#         table_no = int(input("Enter the table number to cancel booking: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         return

#     for table in table_list:
#         if table['table_no'] == table_no:
#             if table['status'] == 'Reserved':
#                 table['status'] = 'Available'
#                 table['reserved_for'] = None
#                 table['reservation_time'] = None
#                 table['reservation_date'] = None
#                 save_tables_to_file(table_list)
#                 print(f"Table {table_no} booking has been canceled.")
#                 return
#             else:
#                 print(f"Table {table_no} is not currently reserved.")
#                 return
#     print("Table not found.")


# # --- Main Program Logic ---
# if __name__ == "__main__":
#     tables_data = load_tables_from_file()

#     while True:
#         print("\n--- Restaurant Management ---")
#         print("1. View Available Tables")
#         print("2. Reserve Table(s)")
#         print("3. Cancel Table Booking")
#         print("4. View Reserved Tables")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             display_available_tables(tables_data)

#         elif choice == '2':
#             try:
#                 num_people_input = int(input("How many people are in your party? "))
#                 if num_people_input <= 0:
#                     print("Number of people must be at least 1.")
#                     continue
#                 reserve_tables_automatically(tables_data, num_people_input)
#             except ValueError:
#                 print("Invalid input. Please enter a valid number.")

#         elif choice == '3':
#             cancel_booking(tables_data)

#         elif choice == '4':
#             display_reserved_tables(tables_data)

#         elif choice == '5':
#             print("Exiting restaurant management system. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")


#22222222222222222222222222222222222222222222222222222222222222


# import json
# import os
# from itertools import combinations
# from datetime import datetime


# TABLES_FILE = "database/tables.json"


# def load_table_data():
#     file_path = 'database/tables.json'
#     if not os.path.exists(file_path):
#         return []
#     with open(file_path, 'r') as file:
#         return json.load(file)


# def load_tables_from_file():
#     """Load tables from JSON file or return default set."""
#     try:
#         if os.path.exists(TABLES_FILE):
#             with open(TABLES_FILE, "r") as file:
#                 return json.load(file)
#     except json.JSONDecodeError:
#         print("Error: Corrupted tables.json. Loading default tables.")

#     # Default tables
#     return [
#         {'table_no': 1, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#         {'table_no': 2, 'status': 'Available', 'occupancy': 2, 'reserved_for': None},
#         {'table_no': 3, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#         {'table_no': 4, 'status': 'Available', 'occupancy': 8, 'reserved_for': None},
#         {'table_no': 5, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#         {'table_no': 6, 'status': 'Available', 'occupancy': 2, 'reserved_for': None},
#         {'table_no': 7, 'status': 'Available', 'occupancy': 6, 'reserved_for': None},
#         {'table_no': 8, 'status': 'Available', 'occupancy': 4, 'reserved_for': None},
#         {'table_no': 9, 'status': 'Available', 'occupancy': 8, 'reserved_for': None},
#         {'table_no': 10, 'status': 'Available', 'occupancy': 2, 'reserved_for': None}
#     ]


# def save_tables_to_file(table_list):
#     with open(TABLES_FILE, "w") as file:
#         json.dump(table_list, file, indent=4)


# def mark_table_available(table_no, table_list):
#     for table in table_list:
#         if str(table["table_no"]) == str(table_no):
#             table["status"] = "Available"
#             table["reserved_for"] = None
#             table["reservation_date"] = None
#             table["reservation_time"] = None
#             return True
#     return False


# # def display_available_tables(table_list):
#     # print("\n--- Available Tables ---")
#     # available = [t for t in table_list if t['status'] == 'Available']
#     # if not available:
#     #     print("No tables currently available.")
#     # else:
#     #     for table in available:
#     #         print(f"Table {table['table_no']} ({table['occupancy']} seater)")
#     # print("------------------------------------")
# def display_available_tables(table_list):
#     table_list = load_tables_from_file()
#     print("\n--- Available Tables ---")
#     available = [t for t in table_list if t['status'] == 'Available']
#     if not available:
#         print("No tables currently available.")
#     else:
#         for table in available:
#             print(f"Table {table['table_no']} ({table['occupancy']} seater)")
#     print("------------------------------------")


# def display_reserved_tables(table_list):
#     """Print all currently reserved tables with details."""
#     print("\n--- Reserved Tables ---")
#     reserved = [t for t in table_list if t['status'] == 'Reserved']
#     if not reserved:
#         print("No tables currently reserved.")
#     else:
#         for t in reserved:
#             print(f"Table {t['table_no']} ({t['occupancy']} seater) - Reserved for {t['reserved_for']} people on {t.get('reservation_date', 'N/A')} at {t.get('reservation_time', 'N/A')}")
#     print("------------------------------------")


# def find_combination_to_fit(table_list, num_people):
#     """Return list of available table(s) that can accommodate given people."""
#     available = [t for t in table_list if t['status'] == 'Available']
#     for r in range(1, len(available) + 1):
#         for combo in combinations(available, r):
#             if sum(t['occupancy'] for t in combo) >= num_people:
#                 return combo
#     return []


# def reserve_tables_automatically(table_list, num_people):
#     """Reserve best fit tables for a group of people."""
#     selected = find_combination_to_fit(table_list, num_people)
#     if not selected:
#         print("No available combination can accommodate this party size.")
#         return

#     while True:
#         reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
#         try:
#             datetime.strptime(reservation_date, "%Y-%m-%d")
#             break
#         except ValueError:
#             print("Invalid format. Please try again.")

#     reservation_time = input("Enter reservation time (e.g. 7:00 PM): ")

#     for table in selected:
#         table['status'] = 'Reserved'
#         table['reserved_for'] = num_people
#         table['reservation_date'] = reservation_date
#         table['reservation_time'] = reservation_time
#         print(f"Table {table['table_no']} ({table['occupancy']} seater) reserved.")

#     save_tables_to_file(table_list)
#     print(f"\n{len(selected)} table(s) reserved for {num_people} people on {reservation_date} at {reservation_time}.")


# def cancel_booking(table_list):
#     """Cancel reservation of a specific table."""
#     try:
#         table_no = int(input("Enter table number to cancel: "))
#     except ValueError:
#         print("Invalid input.")
#         return

#     for table in table_list:
#         if table['table_no'] == table_no:
#             if table['status'] == 'Reserved':
#                 table['status'] = 'Available'
#                 table['reserved_for'] = None
#                 table['reservation_date'] = None
#                 table['reservation_time'] = None
#                 save_tables_to_file(table_list)
#                 print(f"Reservation for Table {table_no} cancelled.")
#                 return
#             else:
#                 print(f"Table {table_no} is not reserved.")
#                 return
#     print("Table not found.")


# # --- Local Run Demo ---
# if __name__ == "__main__":
#     tables_data = load_tables_from_file()

#     while True:
#         print("\n=== Table Booking Menu ===")
#         print("1. View Available Tables")
#         print("2. Reserve Table(s)")
#         print("3. Cancel Table Booking")
#         print("4. View Reserved Tables")
#         print("5. Back to Staff Menu")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             display_available_tables(tables_data)
#         elif choice == '2':
#             try:
#                 num_people = int(input("Enter number of guests: "))
#                 if num_people > 0:
#                     reserve_tables_automatically(tables_data, num_people)
#                 else:
#                     print("Guest count must be at least 1.")
#             except ValueError:
#                 print("Invalid input.")
#         elif choice == '3':
#             cancel_booking(tables_data)
#         elif choice == '4':
#             display_reserved_tables(tables_data)
#         elif choice == '5':
#             print("Returning to Staff Menu...")
#             break
#         else:
#             print("Invalid choice.")


###########
###########################

# import json
# import os
# from database.paths import TABLES_FILE
# from utils.loggers import log_error

# # ---------- Load Table Data ----------
# def load_tables():
#     if os.path.exists(TABLES_FILE):
#         try:
#             with open(TABLES_FILE, "r") as file:
#                 return json.load(file)
#         except Exception as e:
#             log_error(f"Error loading tables: {str(e)}")
#     return {}

# # ---------- Save Table Data ----------
# def save_tables(tables):
#     try:
#         with open(TABLES_FILE, "w") as file:
#             json.dump(tables, file, indent=4)
#     except Exception as e:
#         log_error(f"Error saving tables: {str(e)}")

# # ---------- Reserve a Table ----------
# # def reserve_table(table_no):
# #     tables = load_tables()

# #     if table_no in tables and tables[table_no] == "reserved":
# #         print(f"Table {table_no} is already reserved.")
# #         return

# #     tables[table_no] = "reserved"
# #     save_tables(tables)
# #     print(f"Table {table_no} reserved successfully.")

# def reserve_table(table_no):
#     table_no = int(table_no) 

#     with open(TABLES_FILE, "r") as f:
#         tables = json.load(f)

#     for table in tables:
#         if table["table_no"] == table_no:
#             if table["status"].lower() == "available":
#                 table["status"] = "Reserved"
#                 table["reservation_date"] = input("Enter reservation date (YYYY-MM-DD): ")
#                 table["reservation_time"] = input("Enter reservation time (e.g. 7:30pm): ")
#                 table["reserved_for"] = int(input("How many people? "))
#                 break
#             else:
#                 print("Table is already reserved.")
#                 return

#     with open(TABLES_FILE, "w") as f:
#         json.dump(tables, f, indent=4)
#     print(f"Table {table_no} reserved.")

# # ---------- Free a Table ----------
# def free_table(table_no):
#     tables = load_tables()

#     if table_no in tables and tables[table_no] == "free":
#         print(f"Table {table_no} is already free.")
#         return

#     tables[table_no] = "free"
#     save_tables(tables)
#     print(f"Table {table_no} is now marked as free.")

# # ---------- View All Tables ----------
# def view_tables():
#     tables = load_tables()

#     if not tables:
#         print("No table data found.")
#         return

#     print("\n--- Table Status ---")
#     for table_no, status in sorted(tables.items()):
#         print(f"Table {table_no}: {status.capitalize()}")


# import json
# import os
# from datetime import datetime
# from database.paths import TABLES_FILE
# from utils.loggers import log_error

# # ---------- Load Table Data ----------
# def load_tables():
#     if os.path.exists(TABLES_FILE):
#         try:
#             with open(TABLES_FILE, "r") as file:
#                 return json.load(file)
#         except Exception as e:
#             log_error(f"Error loading tables: {str(e)}")
#     return []

# # ---------- Save Table Data ----------
# def save_tables(tables):
#     try:
#         with open(TABLES_FILE, "w") as file:
#             json.dump(tables, file, indent=4)
#     except Exception as e:
#         log_error(f"Error saving tables: {str(e)}")

# ---------- Reserve a Table ----------
# def reserve_table(table_no):
#     table_no = int(table_no)
#     tables = load_tables()

#     for table in tables:
#         if table["table_no"] == table_no:
#             if table["status"].lower() == "available":
#                 table["status"] = "Reserved"
#                 table["reservation_date"] = input("Enter reservation date (YYYY-MM-DD): ")
#                 table["reservation_time"] = input("Enter reservation time (e.g. 7:30pm): ")
#                 table["reserved_for"] = int(input("How many people? "))
#                 save_tables(tables)
#                 print(f"Table {table_no} reserved.")
#                 return
#             else:
#                 print("Table is already reserved.")
#                 return

#     print(f"Table {table_no} not found.")




# ---------- Free a Table ----------
# def free_table(table_no):
#     table_no = int(table_no)
#     tables = load_tables()

#     for table in tables:
#         if table["table_no"] == table_no:
#             if table["status"].lower() == "available":
#                 print(f"Table {table_no} is already free.")
#             else:
#                 table["status"] = "Available"
#                 table["reservation_date"] = None
#                 table["reservation_time"] = None
#                 table["reserved_for"] = None
#                 save_tables(tables)
#                 print(f"Table {table_no} is now marked as free.")
#             return

#     print(f"Table {table_no} not found.")



# ---------- View All Tables ----------
# def view_tables():
#     tables = load_tables()

#     if not tables:
#         print("No table data found.")
#         return

#     print("\n--- Table Status ---")
#     for table in sorted(tables, key=lambda x: x["table_no"]):
#         print(f"Table {table['table_no']}: {table['status']}")




import json
import os
from datetime import datetime
from database.paths import TABLES_FILE
from utils.loggers import log_error


# ---------- Load Table Data ----------
def load_tables():
    if os.path.exists(TABLES_FILE):
        try:
            with open(TABLES_FILE, "r") as file:
                return json.load(file)
        except Exception as e:
            log_error("Error loading tables: " + str(e))
    return []


# ---------- Save Table Data ----------
def save_tables(tables):
    try:
        with open(TABLES_FILE, "w") as file:
            json.dump(tables, file, indent=4)
    except Exception as e:
        log_error("Error saving tables: " + str(e))


# ---------- Reserve a Table ----------
def reserve_table(table_no):
    table_no = int(table_no)
    tables = load_tables()

    # Ask details
    reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
    start_time = input("Enter start time (e.g. 7:00pm): ")
    end_time = input("Enter end time (e.g. 9:00pm): ")
    # people = int(input("How many people? "))
    # if people > table["capacity"]:
    #     print(f"Cannot reserve: Table {table_no} seats only {table['capacity']} people")
    #     return
    
    try:
        people = int(input("How many people? "))
        if people <= 0:
            print("Number of people must be positive.")
            return
    except ValueError:
        print("Invalid number of people.")
        return

    # Convert to datetime for easy comparison
    try:
        start_dt = datetime.strptime(reservation_date + " " + start_time, "%Y-%m-%d %I:%M%p")
        end_dt = datetime.strptime(reservation_date + " " + end_time, "%Y-%m-%d %I:%M%p")
    except ValueError:
        print("Invalid date/time format.")
        return

    if end_dt <= start_dt:
        print("End time must be after start time.")
        return

    found = False
    for table in tables:
        if table["table_no"] == table_no:
            found = True

            # --- Capacity check ---
            if people > table.get("capacity", 0):
                print(f"Cannot reserve Table {table_no} for {people} people "
                      f"(capacity is {table['capacity']}).")
                return

            # If reserved on same date, check overlap
            if table["status"].lower() == "reserved" and table["reservation_date"] == reservation_date:
                try:
                    existing_start = datetime.strptime(table["reservation_date"] + " " + table["reservation_start_time"], "%Y-%m-%d %I:%M%p")
                    existing_end = datetime.strptime(table["reservation_date"] + " " + table["reservation_end_time"], "%Y-%m-%d %I:%M%p")
                    if start_dt < existing_end and end_dt > existing_start:
                        print(f"Table {table_no} is already reserved during that time.")
                        return
                except Exception:
                    pass  # Ignore old records without proper times

            # Reserve table
            table["status"] = "Reserved"
            table["reservation_date"] = reservation_date
            table["reservation_start_time"] = start_time
            table["reservation_end_time"] = end_time
            table["reserved_for"] = people

            save_tables(tables)
            print("Table", table_no, "reserved from", start_time, "to", end_time, "on", reservation_date)
            return

    if not found:
        print("Table", table_no, "not found.")


# ---------- Free a Table ----------
def free_table(table_no):
    table_no = int(table_no)
    tables = load_tables()

    found = False
    for table in tables:
        if table["table_no"] == table_no:
            found = True
            if table["status"].lower() == "available":
                print("Table", table_no, "is already free.")
            else:
                table["status"] = "Available"
                table["reservation_date"] = None
                table["reservation_start_time"] = None
                table["reservation_end_time"] = None
                table["reserved_for"] = None
                save_tables(tables)
                print("Table", table_no, "is now marked as free.")
            return

    if not found:
        print("Table", table_no, "not found.")


# ---------- View All Tables ----------
def view_tables():
    tables = load_tables()

    if not tables:
        print("No table data found.")
        return

    # sort by table_no
    for i in range(len(tables) - 1):
        for j in range(i + 1, len(tables)):
            if tables[i]["table_no"] > tables[j]["table_no"]:
                tables[i], tables[j] = tables[j], tables[i]


    # Group tables
    reserved_tables = [t for t in tables if t["status"].lower() == "reserved"]
    available_tables = [t for t in tables if t["status"].lower() == "available"]

    print("\n--- Table Status ---")

    # Show reserved tables first
    if reserved_tables:
        print("\n Reserved Tables:")
        for table in reserved_tables:
            print(f"Table {table['table_no']} (Capacity: {table['capacity']}): "
                  f"{table['reservation_date']} from {table['reservation_start_time']} "
                  f"to {table['reservation_end_time']} for {table['reserved_for']} people")

    # Then show available tables
    if available_tables:
        print("\n Available Tables:")
        for table in available_tables:
            print(f"Table {table['table_no']} (Capacity: {table['capacity']})")

    print()  # empty line for spacing

    # print("\n--- Table Status ---")
    # for table in tables:
    #     if table["status"].lower() == "reserved":
    #         print("Table", table["table_no"], ": Reserved on", table["reservation_date"],
    #               "from", table["reservation_start_time"], "to", table["reservation_end_time"],
    #               "for", table["reserved_for"], "people")
    #     else:
    #         print("Table", table["table_no"], ": Available")


