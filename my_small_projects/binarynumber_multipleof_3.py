t=str(input())
while(t):
    decimal=0
    for i in t:
        decimal=decimal*2+int(i)
    if decimal%3==0:
        print 1
    else:
        print 0
    t = t-1
