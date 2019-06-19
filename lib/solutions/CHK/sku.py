class SKU:
    def __init__(self, sku_id, price, discounts=[]):
        self.sku_id = sku_id
        self.price = price
        self.discounts = discounts.sort(key=lambda discount: discount.quantity,reverse=True)
        self.quantity = 0

    def get_price(self, quantity=None):
        if not quantity:
            quantity = self.quantity
        try:
            quantity = int(quantity)
        except ValueError:
            return -1
        if self.discounted_price and self.num_discount:
            return ((quantity // self.num_discount) * self.discounted_price) + (
                (quantity % self.num_discount) * self.price
            )
        if self.discounts:
            return self.apply_discounts(quantity)
        else:
            return quantity * self.price

