class Basket:
    def __init__(self, sku_list=[]):
        self.price_table = {}

        for sku in sku_list:
            self.add_sku(sku)

    def add_sku(self, sku):
        self.price_table[sku.sku_id] = sku

    def incr_sku(self, sku_id):
        self.price_table[sku_id].quantity += 1

    def get_total(self):
        total = 0
        for sku in self.price_table.values():
            if self.discounts.get(sku.sku_id):
                total += self.discounts[sku.sku_id].apply_discount()
            total += sku.get_price()
        return total



    def apply_discounts(self, quantity=None):
        if not quantity:
            quantity = self.quantity
        try:
            quantity = int(quantity)
        except ValueError:
            return -1
        remaining = quantity
        total = 0
        for discount in self.discounts:
            total += (quantity // discount.required_quantity) * discount.price
            remaining -= quantity % discount.required_quantity 
        if remaining > 0:
            total += (remaining * self.price)
        return total
