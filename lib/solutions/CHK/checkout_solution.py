
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from .sku import SKU # need to use relative import because we don't know the structure of  
                     # the test suite.   
    from .basket import Basket
    sku_list = [
      SKU('A', 50, 3, 130),
      SKU('B', 30, 2, 45),
      SKU('C', 20),
      SKU('D', 15)
    ]
    basket = Basket(sku_list)
    # There is no example input which made this all but guarantee a penalty.
    for char in skus:
        try:
            # The spec does not mention quantity so assume it is 1.
            basket.incr_sku(char)
        except (TypeError, KeyError):
            return -1
    return basket.get_total()
