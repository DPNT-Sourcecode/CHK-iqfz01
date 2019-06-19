
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from .sku import SKU # need to use relative import because we don't know the structure of  
                     # the test suite.   
    price_table = {
      'A': SKU('A', 50, 3, 130),
      'B': SKU('B', 30, 2, 45),
      'C': SKU('C', 20),
      'D': SKU('D', 15)
    } 
        
    # There is no example input which made this all but guarantee a penalty.
    total = 0
    for char in skus:
        try:
            # The spec does not mention quantity so assume it is 1.
            total += price_table.get(char).get_price()
        except TypeError:
            return -1
    return total




