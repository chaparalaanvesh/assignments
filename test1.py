def func(a,n):
    count = 0
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[i]+a[j] == n:
                print a[i], a[j], n
                count = count + 1
    print count

a = [1,1,2,2,3,4]
n = 5
func(a,n)
