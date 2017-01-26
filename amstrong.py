def amstrong_num(n):
    sum = 0
    temp = n
    while temp >0:
        digit = temp %10
        sum += digit **3
        temp //= 10
    if n == sum:
        print "amstrong"
    else:
        print "not amstrong"


amstrong_num(407)
