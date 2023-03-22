from classes.order import Order

class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        name

    name = property(get_name, set_name)

    def add_orders(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        customer_list = []
        for order in self.orders():
            if order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list
        
        # the code below is another way of doing the code above - apparently

        # return list(set(map(lambda order: order.customer, self.orders())))

        # list comprehension could also work here!

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total_price = 0

        for order in self.orders():
            total_price += order.price

        return total_price / len(self.orders())