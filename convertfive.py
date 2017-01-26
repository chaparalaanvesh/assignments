def convertFive(n):
    k=0
    while(n!=0):
        result=n%10
        if(result!=0):
            k=k*10+result
        else:
            k=k*10+5
        n=n/10

    while(k!=0):
        r=k%10
        n=n*10+r
        k=k/10

    return n



print convertFive(100)

