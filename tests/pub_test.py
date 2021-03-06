import unittest

from src.pub import Pub 
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100)
        self.customer = Customer("Jenny", 100)
        self.drink_beer = Drink("Beer", 3)
        self.drink_wine = Drink("Wine", 4)
        self.drink_cider = Drink("Cider", 3)
        self.pub.stock_drink = [self.drink_beer, self.drink_wine, self.drink_cider]

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)
    
    def test_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_add_drink(self):
        self.drink_soft = Drink("Soda", 1)
        self.pub.add_drink(self.drink_soft)
        self.assertEqual(4, self.pub.stock_count())

    def test_remove_drink(self):
        self.pub.remove_drink(self.drink_cider)
        self.assertEqual(2, self.pub.stock_count())

    def test_increase_till(self):
        self.pub.increase_till(self.drink_beer)
        self.assertEqual(103, self.pub.till)
        
    def test_sell_drink(self):
        self.pub.sell_drink(self.drink_wine, self.customer)
        self.assertEqual(96, self.customer.wallet)
        self.assertEqual(1, len(self.customer.drinks)) 
        self.assertEqual(104, self.pub.till)
        self.assertEqual(2, self.pub.stock_count())

