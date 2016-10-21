def prime(n):
    l=[]
    if n>0:
        for i in range(n):
            if i%2 == 0:
                l.append(i)
        print "output:",l
    else: print"invalid"

n = input("enter number:")
print "number = ",n
prime(n)