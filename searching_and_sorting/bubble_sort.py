"""bubble sorting technique"""


def bubble_sort( items ) :
    size = len(items)
    for i in range(0,size - 1) :
        for j in range(0, size - i -1) :
            if items[j] > items[j + 1] :
                items[ j ] , items [ j + 1] = items[ j + 1] , items[ j ]


a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a)
print(a)
