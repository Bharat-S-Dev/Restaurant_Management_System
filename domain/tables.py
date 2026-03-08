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


