
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        coffee.add_orders(self)
        customer.add_orders(self)
        Order.all.append(self)