import json
import os
from collections import defaultdict, Counter
from datetime import datetime
from typing import Optional
from database.paths import BILLS_FILE
from utils.loggers import log_error


# === Load Bills ===
def load_bills():
    """Load all bills from JSON file."""
    if not os.path.exists(BILLS_FILE):
        print("No sales data found.")
        return []
    try:
        with open(BILLS_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        log_error(f"Error reading bills.json: {str(e)}")
        print("Failed to load bills.")
        return []


# === Group Sales ===
def group_sales(bills, mode="daily", filter_date: Optional[str] = None):
    sales = {}
    for bill in bills:
        try:
            date_obj = datetime.strptime(bill['datetime'], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue  # Skip invalid datetime format

        if mode == "daily":
            key = date_obj.strftime("%Y-%m-%d")
        elif mode == "weekly":
            year, week, _ = date_obj.isocalendar()
            key = f"{year}-W{week:02d}"
        elif mode == "monthly":
            key = date_obj.strftime("%Y-%m")
        else:
            key = "Unknown"

        if filter_date and not key.startswith(filter_date):
            continue

        if key not in sales:
            sales[key] = {
                'total_revenue': 0.0,
                'tax_collected': 0.0,
                'service_collected': 0.0,
                'discount_given': 0.0,
                'bill_count': 0,
                'items_sold': Counter()
            }

        totals = bill.get('totals', {})
        sales[key]['total_revenue'] += totals.get('grand_total', 0)
        sales[key]['tax_collected'] += totals.get('tax', 0)
        sales[key]['service_collected'] += totals.get('service_charge', 0)
        sales[key]['discount_given'] += totals.get('discount', 0)
        sales[key]['bill_count'] += 1

        for item in bill.get('items', []):
            sales[key]['items_sold'][item['name']] += item['quantity']

    return sales


# === Print Sales Report ===
def print_sales_report(sales, title):
    print(f"\n=======  {title}  =======")
    for key in sorted(sales.keys()):
        data = sales[key]
        print(f"\n Period: {key}")
        print("-" * 40)
        print(f" Total Bills      : {data['bill_count']}")
        print(f" Total Revenue    : Rs.{data['total_revenue']:.2f}")
        print(f" Tax Collected    : Rs.{data['tax_collected']:.2f}")
        print(f" Service Charge   : Rs.{data['service_collected']:.2f}")
        print(f" Discount Given   : Rs.{data['discount_given']:.2f}")
        print("-" * 40)
        print(" Top Items Sold   :")
        print("-" * 40)
        for item, qty in data['items_sold'].most_common(5):
            print(f"   - {item}: {qty} pcs")
        print("-" * 40)


# === New: Show All Bills ===
def show_all_bills():
    """Display all bills in a simple list format."""
    bills = load_bills()
    if not bills:
        return

    print("\n=== All Bills ===")
    for bill in bills:
        print(f"Bill ID       : {bill['bill_id']}")
        print(f"Customer      : {bill['customer']}")
        print(f"Table No.     : {bill['table_no']}")
        print(f"Date & Time   : {bill['datetime']}")
        print(f"Total Amount  : Rs.{bill['totals']['grand_total']:.2f}")
        print("-" * 40)


# === New: Show Daily Sales for Today ===
def show_daily_sales():
    """Show today's sales summary."""
    today = datetime.today().strftime("%Y-%m-%d")
    bills = load_bills()
    if not bills:
        return
    sales = group_sales(bills, mode="daily", filter_date=today)
    print_sales_report(sales, f"SALES REPORT FOR {today}")


# === Main Report Menu ===
# def generate_report():
#     bills = load_bills()
#     if not bills:
#         return

#     print("\n=== Sales Report Menu ===")
#     print("1. Daily report")
#     print("2. Weekly summary")
#     print("3. Monthly summary")
#     print("4. Filter by specific date (YYYY-MM-DD)")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         sales = group_sales(bills, mode="daily")
#         print_sales_report(sales, "DAILY SALES REPORT")
#     elif choice == "2":
#         sales = group_sales(bills, mode="weekly")
#         print_sales_report(sales, "WEEKLY SALES SUMMARY")
#     elif choice == "3":
#         sales = group_sales(bills, mode="monthly")
#         print_sales_report(sales, "MONTHLY SALES SUMMARY")
#     elif choice == "4":
#         date = input("Enter date (YYYY-MM-DD): ")
#         try:
#             datetime.strptime(date, "%Y-%m-%d")
#         except ValueError:
#             print("Invalid date format.")
#             return
#         sales = group_sales(bills, mode="daily", filter_date=date)
#         print_sales_report(sales, f"SALES REPORT FOR {date}")
#     else:
#         print("Invalid choice.")


def generate_report():
    bills = load_bills()
    if not bills:
        return

    while True:
        print("\n=== Sales Report Menu ===")
        print("1. Show All Bills")
        print("2. Today's Sales Summary")
        print("3. Daily report")
        print("4. Weekly summary")
        print("5. Monthly summary")
        print("6. Filter by specific date (YYYY-MM-DD)")
        print("7. Exit Reports Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_all_bills()

        elif choice == "2":
            today = datetime.today().strftime("%Y-%m-%d")
            print(f"\n  Today's Date: {today}")
            show_daily_sales()

        elif choice == "3":
            sales = group_sales(bills, mode="daily")
            print_sales_report(sales, "DAILY SALES REPORT")

        elif choice == "4":
            sales = group_sales(bills, mode="weekly")
            print_sales_report(sales, "WEEKLY SALES SUMMARY")

        elif choice == "5":
            sales = group_sales(bills, mode="monthly")
            print_sales_report(sales, "MONTHLY SALES SUMMARY")

        elif choice == "6":
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format.")
                continue
            sales = group_sales(bills, mode="daily", filter_date=date)
            print_sales_report(sales, f"SALES REPORT FOR {date}")

        elif choice == "7":
            print("Exiting Reports Menu...")
            break

        else:
            print("Invalid choice. Please try again.")
