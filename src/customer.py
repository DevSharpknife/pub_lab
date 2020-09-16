class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def decrease_wallet(self, drink):
        self.wallet -= drink.price

    # def buy_drink(self, drink):


