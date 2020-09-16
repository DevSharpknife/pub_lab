import unittest

from src.pub import Pub 
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.drink_beer = Drink("Beer", 3.5)
        self.drink_wine = Drink("Wine", 4)
        self.drink_cider = Drink("Cider", 3)
        self.pub.stock_drink = [self.drink_beer, self.drink_wine, self.drink_cider]

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_add_drink(self):
        self.drink_soft = Drink("Soda", 1.5)
        self.pub.add_drink(self.drink_soft)
        self.assertEqual(4, self.pub.stock_count())