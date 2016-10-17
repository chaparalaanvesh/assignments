import sys
list1 = [10,9,6,8,2,4,3,7,1,5]
list2 = []
for i in range(len(list1)):
    temp = min(list1)
    list2.append(temp)
    list1.remove(temp)

print list2