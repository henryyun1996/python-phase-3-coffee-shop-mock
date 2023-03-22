from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and ( len(name) > 0 and len(name) < 16 ):
            self._name = name
    
    name = property(get_name, set_name)

    def add_orders(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(map(lambda order: order.coffee, self.orders())))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)