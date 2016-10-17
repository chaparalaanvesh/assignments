import sys
n = int(raw_input('enter number:'))
s = '#'
for i in range( 1 , n+1):
    print " "*(n-i) + s*i