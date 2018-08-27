import uuid

from datetime import datetime

items_list = []


class Items:
    def __init__(
            self, item_name, unit_price, purchase_price, quantity, quantity_sold, balance, amount
    ):
        self.item_id = uuid.uuid4().int
        self.date_added = datetime.utcnow()
        self.item_name = item_name
        self.unit_price = unit_price
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.quantity_sold = quantity_sold
        self.balance = balance
        self.amount = amount

    def __repr__(self):
        return {
            'item_id': self.item_id,
            'date_added': self.date_added,
            'item_name': self.item_name,
            'unit_name': self.unit_price,
            'purchase_price': self.purchase_price,
            'quantity': self.quantity,
            'quantity_sold': self.quantity_sold
        }

    def sell_item(self, item):
        if item:
            items_list.append(item)
            self.amount = (self.quantity*self.purchase_price)
        return "Item sold"

    def update_balance(self):
        self.balance = len(items_list) - self.quantity
        return self.balance

    def update_unit_price(self, unit_price):
        self.unit_price = unit_price
