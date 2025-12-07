import json
import os
from datetime import datetime
from abc import ABC, abstractmethod
from uuid import uuid4

from domain.menu.menu_data import load_menu
from database.paths import MENU_FILE, ORDERS_FILE, BILLS_FILE, TABLES_FILE
from utils.loggers import log_error


# ------------------ Payment Gateway ------------------

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Collect cash: Rs.{amount:.2f}")
        print("Payment successful (Cash)")

class CardPayment(PaymentGateway):
    def pay(self, amount):
        card = input("Enter card number: ")
        print(f"Processing card ending {card[-4:]} for Rs.{amount:.2f}...")
        print("Payment successful (Card)")

class UPIPayment(PaymentGateway):
    def pay(self, amount):
        upi = input("Enter UPI ID: ")
        print(f"Requesting Rs.{amount:.2f} from {upi}...")
        print("Payment successful (UPI)")


# ------------------ Bill Class ------------------

class Bill:
    def __init__(self, customer_name, table_no):
        self.customer_name = customer_name
        self.table_no = str(table_no)  # Store as string to match JSON keys
        self.bill_id = f"BILL{str(uuid4())[:8].upper()}"
        self.items = []
        self.subtotal = 0
        self.discount = 0
        self.tax_rate = 0.05
        self.service_charge_rate = 0.10
        self.menu = load_menu()

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            self.discount = percent / 100
            print(f"Discount of {percent}% applied.")
        else:
            print("Invalid discount.")

    def add_order_items(self, order_items):
        for item in order_items:
            self.items.append(item)
            self.subtotal += item['total_price']

    def calculate_total(self):
        discount_amt = self.subtotal * self.discount
        discounted_subtotal = self.subtotal - discount_amt
        tax = discounted_subtotal * self.tax_rate
        service = discounted_subtotal * self.service_charge_rate
        total = discounted_subtotal + tax + service
        return {
            'subtotal': self.subtotal,
            'discount': discount_amt,
            'discounted_subtotal': discounted_subtotal,
            'tax': tax,
            'service_charge': service,
            'grand_total': total
        }

    def print_receipt(self):
        totals = self.calculate_total()
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        print("\n" + "=" * 60)
        print("            RESTAURANT INVOICE RECEIPT")
        print("=" * 60)
        print(f"Bill ID       : {self.bill_id}")
        print(f"Customer Name : {self.customer_name}")
        print(f"Table No.     : {self.table_no}")
        print(f"Date & Time   : {now}")
        print("-" * 60)
        print(f"{'Item':25} {'Size':>6} {'Qty':>5} {'Rate':>7} {'Total':>8}")
        print("-" * 60)
        for item in self.items:
            print(f"{item['name'][:25]:25} {item['portion']:>6} {item['quantity']:>5} "
                  f"{item['unit_price']:>7.2f} Rs.{item['total_price']:>7.2f}")
        print("-" * 60)
        print(f"Subtotal       : Rs{totals['subtotal']:.2f}")
        if self.discount > 0:
            print(f"Discount ({int(self.discount * 100)}%) : -Rs{totals['discount']:.2f}")
        print(f"Tax (5%)       : Rs{totals['tax']:.2f}")
        print(f"Service (10%)  : Rs{totals['service_charge']:.2f}")
        print(f"Total          : Rs{totals['grand_total']:.2f}")
        print("=" * 60)
        print("         Thank you for dining with us! ")
        print("        Follow us on Instagram: @myrestaurant")
        print("=" * 60)

    def process_payment(self):
        totals = self.calculate_total()
        print("\n-- Payment Options --")
        print("1. Cash")
        print("2. Card")
        print("3. UPI")
        try:
            method = int(input("Choose: "))
        except ValueError:
            print("Invalid input.")
            return

        if method == 1:
            gateway = CashPayment()
        elif method == 2:
            gateway = CardPayment()
        elif method == 3:
            gateway = UPIPayment()
        else:
            print("Invalid choice.")
            return

        gateway.pay(totals['grand_total'])

    def save_invoice_txt(self):
        totals = self.calculate_total()
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        filename = f"invoices/{self.bill_id}.txt"
        os.makedirs("invoices", exist_ok=True)

        with open(filename, "w") as f:
            f.write("=" * 60 + "\n")
            f.write("         RESTAURANT INVOICE RECEIPT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Bill ID       : {self.bill_id}\n")
            f.write(f"Customer Name : {self.customer_name}\n")
            f.write(f"Table No.     : {self.table_no}\n")
            f.write(f"Date & Time   : {now}\n")
            f.write("-" * 60 + "\n")
            f.write(f"{'Item':15} {'Size':>6} {'Qty':>5} {'Rate':>7} {'Total':>8}\n")
            f.write("-" * 60 + "\n")
            for item in self.items:
                f.write(f"{item['name'][:15]:15} {item['portion']:>6} {item['quantity']:>5} "
                        f"{item['unit_price']:>7.2f} {item['total_price']:>8.2f}\n")
            f.write("-" * 60 + "\n")
            f.write(f"{'Subtotal':30} Rs{totals['subtotal']:>10.2f}\n")
            if self.discount > 0:
                f.write(f"{f'Discount ({int(self.discount * 100)}%)':30}-Rs.{totals['discount']:>10.2f}\n")
            f.write(f"{'Tax (5%)':30} Rs{totals['tax']:>10.2f}\n")
            f.write(f"{'Service Charge (10%)':30} Rs{totals['service_charge']:>10.2f}\n")
            f.write("=" * 60 + "\n")
            f.write(f"{'Grand Total':30} Rs.{totals['grand_total']:>10.2f}\n")
            f.write("=" * 60 + "\n")
            f.write("      Thank you! Visit Again \n")
            f.write("   Follow us on IG: @myrestaurant\n")
            f.write("=" * 60 + "\n")

        print(f"Invoice saved as: {filename}")

    def save_to_file(self):
        bill_data = {
            'bill_id': self.bill_id,
            'customer': self.customer_name,
            'table_no': self.table_no,
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'discount_percent': int(self.discount * 100),
            'items': self.items,
            'totals': self.calculate_total()
        }

        all_bills = []
        if os.path.exists(BILLS_FILE):
            try:
                with open(BILLS_FILE, "r") as file:
                    all_bills = json.load(file)
            except Exception as e:
                log_error(f"Failed to load bills: {str(e)}")

        all_bills.append(bill_data)

        with open(BILLS_FILE, "w") as file:
            json.dump(all_bills, file, indent=4)

        self.save_invoice_txt()
        self.clear_order_and_free_table()

    def clear_order_and_free_table(self):
        # Remove order from orders.json
        try:
            with open(ORDERS_FILE, "r") as file:
                orders = json.load(file)
        except:
            orders = {}

        if self.table_no in orders:
            del orders[self.table_no]
            with open(ORDERS_FILE, "w") as file:
                json.dump(orders, file, indent=4)
            print("-"*40)
            print(f"Order for table {self.table_no} removed after billing.")

        # Free table in tables.json
        try:
            with open(TABLES_FILE, "r") as file:
                tables = json.load(file)
        except:
            tables = []

        for table in tables:
            if str(table["table_no"]) == str(self.table_no):
                table["status"] = "Available"
                table["reservation_date"] = None
                table["reservation_start_time"] = None
                table["reservation_end_time"] = None
                table["reserved_for"] = None
                break

        with open(TABLES_FILE, "w") as file:
            json.dump(tables, file, indent=4)

        print(f"Table {self.table_no} is now marked as Available.")


# ------------------ Billing Entry Point ------------------

def generate_bill(table_no):
    table_no = str(table_no)
    try:
        with open(ORDERS_FILE, "r") as file:
            orders = json.load(file)
    except FileNotFoundError:
        print("No orders found.")
        return
    except Exception as e:
        log_error(f"Failed to load orders: {str(e)}")
        return

    if table_no not in orders:
        print(f"No active order for table {table_no}")
        return

    customer_name = input("Enter customer name: ")
    order_data = orders[table_no]
    items = order_data["items"]

    bill = Bill(customer_name, table_no)
    bill.add_order_items(items)

    try:
        use_discount = input("Apply discount? (yes/no): ").lower()
        if use_discount == "yes":
            percent = int(input("Enter discount %: "))
            bill.apply_discount(percent)
    except:
        print("Skipping discount.")

    bill.print_receipt()
    bill.process_payment()
    bill.save_to_file()
