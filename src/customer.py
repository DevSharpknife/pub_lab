class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks = []
    
    def decrease_wallet(self, drink):
        self.wallet -= drink.price

    def add_drink_to_customer(self, drink):
        self.drinks.append(drink)
        