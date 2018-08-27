import uuid


class User:

    def __init__(self, user_role, username, password, login_timestamp):
        self.user_id = uuid.uuid4().int
        self.user_role = user_role
        self.username = username
        self.password = password
        self.login_timestamp = login_timestamp

    def __repr__(self):
        return {
            'user_id': self.user_id,
            'user_role': self.user_role,
            'username': self.username,
            'password': self.password,
            'login_timestamp': self.login_timestamp
        }

    def view_daily_sales(self, item_id):
        """View daily sales per item. Must be authorized"""
        # TODO

    def view_stock_balance(self, item_id):
        """View stock balance for specific item"""
        # TODO

    def add_stock_item(self, item_id, quantity):
        """Add quantity to stock of a specific item"""
        # TODO

    def update_stock(self, item_id, quantity):
        """Update stock balance for a specific item"""
        # TODO


class StockItem:

    def __init__(self, item_code, name, date_added, purchace_price, unit_price, stock_quantity, sold_quantity, added_by):
        self.item_code = item_code
        self.name = name
        self.date_added = date_added
        self.purchace_price = purchace_price
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity
        self.sold_quantity = sold_quantity
        self.added_by = added_by

