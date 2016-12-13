def count():
    str = 'I saw that this post was very similar to another one so I believed that they were the same'
    char = ['a','c','e','d','i','o','g','u','s','z']
    list = []
    for i in str:
        if i in char:
            list.append(i)
    print list
    list2 = {x:list.count(x) for x in list}
    print list2

    for j in range(len(list2)):
        for k in range(len(list2)-1):
            if list2[k]>  list2[k+1]:
                temp = list2[k]
                list2[k] = list2[k+1]
                list2[k] = temp
    print char(list2)
count()
