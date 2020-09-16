
class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock_drink = []
    
    def add_drink(self, drink):
        self.stock_drink.append(drink)

    def stock_count(self):
        return len(self.stock_drink)

#A Customer should be able to buy a Drink from the Pub, reducing the money in its wallet and increasing the money in the Pub's till

    def sell_drink(self, drink):
        self.till += drink.price
    #     self.stock_drink -= 1
    #     self.customer.decrease_wallet(drink.price)
        



# def pay_drink

# def sell_drin(self.):
#     pay.drink()
#     charge.customer()