def is_palindrome():
    a = raw_input("enter a string: ")
    print a
    print list(a)
    if a.upper()[:] == a.upper()[::-1]:
        print "palindrome"
    else:
        print "not palindrome"
is_palindrome()


