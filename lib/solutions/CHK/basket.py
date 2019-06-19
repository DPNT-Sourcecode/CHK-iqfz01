def get_total(order_string):
    total = 0
    # the previous implementation got a little complicated,
    # so for expediency we will just calculate very simply
    # until we know or can limit the precise format of our discounts
    # which is simpler from an operational standpoint and for the customer.

    num_a = order_string.count('A')
    a_discount_one = num_a // 5 #quantity divisible by 5, for first discount
    a_discount_two = (num_a % 5) // 3 # quantity div. by 3 for second discount
    a_remain = num_a - (a_discount_one * 5) - (a_discount_two * 3)
    total += (((
        a_discount_one  * 200
    ) + 
        a_discount_two *  130
    ) + (a_remain * 50))

    # do e next so we can discount b more easily
    num_e = order_string.count('E')
    free_b = num_e // 2
    total += num_e * 40
    
    # b
    num_b = order_string.count('B') - free_b
    total += (
        (num_b // 2) * 45
    ) + (num_b % 2 * 30)

    # c and d
    total += order_string.count('C') * 20
    total += order_string.count('D') * 15


    # we don't need to return -1 anymore, as any string is valid
    # in this implementation. We could reject srings not containing
    # SKU IDs we possess, but the spec does not ask for this
    # so behaviour may be unexpected.
    return total

