class SKU:

    def __init__(self, sku_id, price, num_discount=None, discounted_price=None):
        self.sku_id = sku_id
        self.price = price
        self.discounted_price = discounted_price
        self.num_discount = num_discount

    def get_price(self, quantity):
        try:
            quantity = int(quantity)
        except ValueError:
            return -1
        if self.discounted_price and self.num_discount:
            return (
                (quantity // self.num_discount) * self.discounted_price
            ) + 
            (
                (quantity % self.num_discount) * self.price
            )
        else:
            return quantity * self.
            