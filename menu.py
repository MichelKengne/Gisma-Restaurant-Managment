"""A menu for thr GISMA Restaurant.""" 

class MenuItems:
   
    def __init__(self, itemID, name, price):
        self.itemID = itemID
        self.name = name
        self.price = float(price)
    
    def get_details(self):
        return f"{self.itemID}: {self.name} - ${self.price:.2f}"
    
    def update_price(self, new_price):
        self.price = float(new_price)
        return True
    
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name


  