class Basket:
    def __init__(self, sku_list=[]):
        self.price_table = {}

        for sku in sku_list:
            self.add_sku(sku)
            
    def add_sku(self, sku):
        self.price_table[sku.sku_id] = sku


    def get_total(self):
        total = 0
        for sku in self.price_table.values():
            total += sku.get_price()
        return total
