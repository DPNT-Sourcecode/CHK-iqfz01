
class Discount:
    pass

class MultiBuyDiscount(Discount):
    def __init__(self, sku, number, discounted_price)
        pass

    def apply(self, quantity)
        pass

class BuyFreeDiscount(Discount):
    def __init__(self, number, free_sku)
        pass
    def apply_discount(self)
        pass