class Basket:

    def __init__(self, sku_list=[]):
        self.price_table = {}

        for sku in sku_list:
            self.price_table[sku.sku_id] = sku



    def get_total(self):
        