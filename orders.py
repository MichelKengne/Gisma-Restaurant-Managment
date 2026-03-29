""""Order class which manages everything related to the orders with an Example of usage"""

class Order:
    def __init__(self, order_id, table_number):
        self.order_id = order_id
        self.table_number = table_number
        self.items = []
        self.status = "Open"

    def add_item(self, item_id, quantity=1):
        self.items.append((item_id, quantity))
        return True

    def calculate_total(self, menu_items):
        total = 0
        for item_id, quantity in self.items:
            for item in menu_items.values():
                if item.itemID == item_id:
                    total += item.price * quantity
                    break
        return total

    def get_order_details(self, menu_items):
        details = []
        for item_id, quantity in self.items:
            for item in menu_items.values():
                if item.itemID == item_id:
                    details.append(f"{item.name} x{quantity} - ${item.price * quantity:.2f}")
                    break
        return details

    def close(self):
        self.status = "Closed"
        return True