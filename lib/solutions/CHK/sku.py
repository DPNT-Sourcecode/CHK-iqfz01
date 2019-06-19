class SKU:
    def __init__(self, sku_id, price, num_discount=None, discounted_price=None):
        self.sku_id = sku_id
        self.price = price
        self.discounted_price = discounted_price
        self.num_discount = num_discount
        self.quantity = 0

    def get_price(self):

        if self.discounted_price and self.num_discount:
            return ((self.quantity // self.num_discount) * self.discounted_price) + (
                (self.quantity % self.num_discount) * self.price
            )
        else:
            return self.quantity * self.price
