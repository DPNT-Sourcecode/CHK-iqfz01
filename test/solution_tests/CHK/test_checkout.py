from solutions.CHK.sku import SKU
import unittest

class TestSum(unittest.TestCase):

    def test_sku(self, *args, **kwargs):
        
        a = SKU('A', 50, 3, 130)
        b = SKU('B', 30, 2, 45)
        c = SKU('C', 20)
        d = SKU('D', 15)

        self.assertEqual(a.get_price(3), 130)
        self.assertEqual(b.get_price(2), 45)
        