
def items():
    curr_item = raw_input("enter item:")
    cart = []
    f = open('items_list.txt')
    if curr_item in f.read():
         cart.append(curr_item)

    else:
        return "Item not available"
    return cart
    f.close()


print items()
