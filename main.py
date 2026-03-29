"""Main program - interactive menu for the restaurant."""

from restaurant import Restaurant
from menu import MenuItems
from tables import Table


def main():
    rest = Restaurant()

    # Add 5 default tables if none exist
    if not rest.tables:
        for i in range(1, 6):
            capacity = 4 if i <= 3 else 6
            rest.add_table(Table(i, capacity))

    while True:
        print("\n=== Gisma Restaurant Management System ===")
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Add New Table")
        print("4. Create New Order")
        print("5. Add Item to Order")
        print("6. View Open Orders")
        print("7. Close Order & Generate Bill")
        print("8. Save & Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            iid = input("Item ID: ")
            name = input("Name: ")
            price = input("Price: ")
            item = MenuItems(iid, name, price)
            rest.add_menu_item(item)
            print("Menu item added successfully.")

        elif choice == "2":
            for item in rest.view_menu():
                print(item)

        elif choice == "3":
            tnum = int(input("Table number: "))
            cap = int(input("Capacity (default 4): ") or 4)
            rest.add_table(Table(tnum, cap))
            print("Table added successfully.")

        elif choice == "4":
            tnum = int(input("Table number: "))
            oid = rest.create_order(tnum)
            if oid:
                print(f"Order #{oid} created for Table {tnum}.")
            else:
                print("Table not found.")

        elif choice == "5":
            oid = int(input("Order ID: "))
            iid = input("Item ID: ")
            qty = int(input("Quantity (default 1): ") or 1)
            if rest.add_item_to_order(oid, iid, qty):
                print("Item added successfully.")
            else:
                print("Invalid order or item.")

        elif choice == "6":
            orders = rest.view_orders()
            if orders:
                for order_details in orders:
                    for line in order_details:
                        print("-" * 40)
            else:
                print("No open orders.")

        elif choice == "7":
            oid = int(input("Order ID to close: "))
            total = rest.close_order(oid)
            if total is not None:
                print(f"Order #{oid} closed. Bill: ${total:.2f}")
            else:
                print("Order not found.")

        elif choice == "8":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()