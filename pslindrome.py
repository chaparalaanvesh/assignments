def palindrome(a):
    for i in range (0, len(a)/ 2):
        if a[i] == a[(i * -1) - 1]:
            print 'is palindrome'
        else:
           print 'not a palindrome'

n = raw_input("enter string:")
palindrome(n)
