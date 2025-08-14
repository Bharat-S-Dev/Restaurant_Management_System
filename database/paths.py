# database/paths.py


# BILLS_FILE = "database/bills.json"
# MENU_FILE = "database/menu.json"
# ORDERS_FILE = "database/orders.json"
# TABLES_FILE = "database/tables.json"



# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# MENU_FILE = os.path.join(BASE_DIR, 'database', 'menu.json')
# ORDERS_FILE = os.path.join(BASE_DIR, 'database', 'orders.json')
# BILLS_FILE = os.path.join(BASE_DIR, 'database', 'bills.json')
# TABLES_FILE = os.path.join(BASE_DIR, 'database', 'tables.json')
# USERS_FILE = os.path.join(BASE_DIR, 'database', 'users.json')

import os

# Base folder for database files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to each JSON file
USERS_FILE = os.path.join(BASE_DIR, "users.json")
MENU_FILE = os.path.join(BASE_DIR, "menu.json")
ORDERS_FILE = os.path.join(BASE_DIR, "orders.json")
BILLS_FILE = os.path.join(BASE_DIR, "bills.json")
TABLES_FILE = os.path.join(BASE_DIR, "tables.json")
