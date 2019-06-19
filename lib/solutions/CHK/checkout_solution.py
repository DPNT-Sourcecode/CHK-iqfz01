
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # need to use relative import because we don't know the structure of  
    # the test suite.   
    from .basket import get_total
    
    return get_total(skus)

