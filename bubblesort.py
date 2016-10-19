
l = [10,5,4,3,1]
i = 0
for i in range(len(l)-1):
    if l[i] > l[i+1]:
        temp = l[i]
        l[i] = l[i+1]
        l[i+1] = temp
    print l