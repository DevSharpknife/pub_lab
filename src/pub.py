
class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock_drink = []
    
    def add_drink(self, drink):
        self.stock_drink.append(drink)

    def stock_count(self):
        return len(self.stock_drink)