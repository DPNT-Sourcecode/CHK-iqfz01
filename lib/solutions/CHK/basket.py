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
        # so for expediency we will just calculate very simply
        # until we know or can limit the precise format of our discounts
        # which is simpler from an operational standpoint and for the customer.

        num_a = order_string.count('A')
        a_discount_one = num_a // 5 #quantity divisible by 5, for first discount
        a_discount_two = (num_a - (num_a % 5)) // 3 # quantity div. by 3 for second discount
        a_remain = num_a - (a_discount_one * 5) - a_discount_two * 3  # remaining quantity for leftover pricing
        total += (
            a_discount_one  * 200
        ) + (
            a_discount_two *  150
        ) + (a_remain * 50)

