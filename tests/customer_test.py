import unittest

from src.pub import Pub 
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Bill", 50.0)

    # def test_can_decrease_wallet(self):
    #     self.customer.decrease_wallet()
    #     self.assertEqual(46.0, self.customer.wallet)
