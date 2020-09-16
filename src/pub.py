
class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock_drink = []
    
    def add_drink(self, drink):
        self.stock_drink.append(drink)

    def remove_drink(self, drink):
        self.stock_drink.remove(drink)

    def stock_count(self):
        return len(self.stock_drink)

    def increase_till(self, drink):
        self.till += drink.price

    def sell_drink(self, drink, customer):
        customer.decrease_wallet(drink)
        customer.add_drink_to_customer(drink)
        self.increase_till(drink)
        self.remove_drink(drink)
     

