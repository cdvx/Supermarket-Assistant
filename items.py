import uuid
from  datetime import datetime

class Items(object):
    '''This class defines Items'''

    def __init__(self, date_added, item_name, purchase_price, 
               unit_price, quantity, quantity_sold, added_by):
               self.item_id = uuid.uuid4().int
               self.date_added = datetime.utcnow()
               self.item_name = item_name
               self.purchase_price = purchase_price
               self.unit_price = unit_price
               self.quantity = quantity
               self.quantity_sold = quantity_sold
               self.added_by = added_by

    def __repr__(self):
        return {
            'item_id': self.item_id,
            'date_added': self.date_added
            'item_name': self.item_added
            'purchase_price': self.purchase_price
            'unit_price': self.unit_price
            'quantity': self.quantity
            'quantity_sold': self.quantity_sold
            'added_by': self.added_by
        }

    def add_item(self, item_name, date-added, quantity, unit_price):
        pass
        

    def update_balances(self):
        pass


    def update_unit_price(self):
        pass





