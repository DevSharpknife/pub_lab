import unittest

from src.pub import Pub 
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Bill", 50.0)

    def test_can_decrease_wallet(self):
        self.customer.decrease_wallet(30)
        self.assertEqual(20, self.customer.wallet)