from lib.solutions.CHK.checkout_solution import checkout
import unittest

class TestCheckout(unittest.TestCase):
    
    def test_total(self, *args, **kwargs):
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout(''), 0)
        self.assertEqual(checkout('AAA'), 130)
        self.assertEqual(checkout('AAABB'), 175)
        self.assertEqual(checkout('AAAA'), 180)
        self.assertEqual(checkout('AAAABB'), 225)
        self.assertEqual(checkout('AAAABBBEE'), 305)
        self.assertEqual(checkout('AAAABBBBEE'), 335)
        self.assertEqual(checkout('AAAABBBBEECD'), 370)
        self.assertEqual(checkout('a'), -1)
        self.assertEqual(checkout('EE'), 80)
        self.assertEqual(checkout('F'), 10)
        self.assertEqual(checkout('FF'), 20)
        self.assertEqual(checkout('FFF'), 30)
        self.assertEqual(checkout('FFFF'), 40) 
        self.assertEqual(checkout('AAAABBBBEECDFF'), 390)
        self.assertEqual(checkout('AAAABBBBEECDFFF'), 390)
        
