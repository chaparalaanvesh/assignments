import sys
number = input('enter value:')
print number
if(number%2 == 0):
    print 'it is even number'
    if(number%4 == 0):
        print 'it is also a multiple of 4'
    else:
        print ''
else:
    print 'it is odd number'