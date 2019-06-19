class SKU:

    def __init__(self, sku_id, price, num_discount=None, discounted_price=None):
        self.sku_id = sku_id
        self.price = price
        self.discounted_price = discounted_price
        self.num_discount = num_discount

    def get_price(self, quantity):
        pass