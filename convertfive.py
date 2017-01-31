#converting all the 0's to 5 in the given integer



def convertFive(n):
    list1 = map(int,str(n))
    temp = [5 if x==0 else x for x in list1]
    a = map(str, temp)
    result=''.join(a)
    return result

print convertFive(100)
print convertFive(121)
print convertFive(100500)
