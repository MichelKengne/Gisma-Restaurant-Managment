""""Restaurant class which manages everything related to the restaurant"""

import csv
from menu import MenuItems
from orders import Order
from tables import Table

class Restaurant:
    def __init__(self):
        self.menu = {}
        self.orders = {}
        self.tables = {}
        self.next_order_id = 1

    def add_menu_item(self, item):
        self.menu[item.itemID] = item

    def add_table(self, table):
        self.tables[table.table_number] = table

    def create_order(self, table_number):
        if table_number not in self.tables:
            return None
        order = Order(self.next_order_id, table_number)
        self.orders[self.next_order_id] = order
        self.tables[table_number].assign_order(self.next_order_id)
        self.next_order_id += 1
        return order.order_id
    
    def add_item_to_order(self, order_id, item_id, quantity=1):
        if order_id in self.orders and item_id in self.menu:
            self.orders[order_id].add_item(item_id, quantity)
            return True
        return False
    
    def view_menu(self):
        return [item.get_details() for item in self.menu.values()]

    def view_orders(self):
        return [order.get_details(self.menu) 
                for order in self.orders.values()
                if order.status == "Open"]

    def close_order(self, order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            total = order.calculate_total(self.menu)
            order.close()
            table_num = order.table_number
            if table_num in self.tables:
                self.tables[table_num].free_table()
            return total
        return None
    

