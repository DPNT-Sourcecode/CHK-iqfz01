from lib.solutions.CHK.sku import SKU
from lib.solutions.CHK.checkout_solution import checkout
import unittest

class TestCheckout(unittest.TestCase):

    
    def test_sku(self, *args, **kwargs):
        
        a = SKU('A', 50, 3, 130)
        b = SKU('B', 30, 2, 45)
        c = SKU('C', 20)
        d = SKU('D', 15)
    
        self.assertEqual(a.get_price(0), 0)
        self.assertEqual(a.get_price(1), 50) 
        self.assertEqual(a.get_price(3), 130)
        self.assertEqual(b.get_price(2), 45)
        self.assertEqual(a.get_price(4), 180)
        self.assertEqual(a.get_price(6), 260)
        self.assertEqual(b.get_price(3), 75)
        self.assertEqual(c.get_price(10), 200)
        self.assertEqual(d.get_price(3), 45)
        self.assertEqual(a.get_price('kitties'), -1)
        
    
        
    def test_total(self, *args, **kwargs):
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout(''), -1)
        self.assertEqual(checkout('AB'))
        
        
