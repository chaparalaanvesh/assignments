"""Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.
For example:
Given num = 89, the process is like: 8 + 9 = 17, 1 + 7 = 8. Since 2 has only
one digit, return it."""



n = input("enter a number:")
a = list(str(n))
if len(a) < 2:
    print str(n)
else:
    for i in a:
        numlist = map(int, a)
        s = sum(numlist)
    print s

if s>9:
    b = list(str(s))
    for j in b:
        numlist1 = map(int,b)
        s1 = sum(numlist1)
    print s1

