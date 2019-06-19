class Basket:
    def __init__(self, sku_list=[]):
        self.price_table = {}

        for sku in sku_list:
            self.add_sku(sku)

    def add_sku(self, sku):
        self.price_table[sku.sku_id] = sku

    def incr_sku(self, sku_id):
        self.price_table[sku_id].quantity += 1

    def get_total(self, order_string):
        total = 0
        # the previous implementation got a little complicated,
        # so for expediency we will just calculate very simply.

        num_a = order_string.count('A')

        total += (num_a)

