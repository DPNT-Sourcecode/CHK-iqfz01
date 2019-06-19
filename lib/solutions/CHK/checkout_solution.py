
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from .sku import SKU # need to use relative import because we don't know the structure of  
                     # the test suite.   

    # There is no example input which made this all but guarantee a penalty.
    for char in skus:



