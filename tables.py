"""Table class which manages everything related to the tables"""

class Table:
    def __init__(self, table_number, capacity=4):
        self.table_number = table_number
        self.capacity = capacity
        self.is_occupied = False
        self.current_orderID = None

    def occupy_table(self, order):
        if not self.is_occupied:
            self.is_occupied = True
            self.current_orderID = order.order_ID
            
    def free_table(self):
        self.is_occupied = False
        self.current_orderID = None

    def get_table_status(self):
        return f"Table {self.table_number} - Capacity: {self.capacity} - {'Occupied' if self.is_occupied else 'Available'}"
    
    def assign_order(self, order_ID):
        self.current_orderID = order_ID
        self.occupy_table(order_ID)
       