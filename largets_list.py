def largest_number():
    list = lambda i,j: i if i>j else j

    result = reduce(list,[1,2,3,55,6,88])
    return result

print largest_number()
