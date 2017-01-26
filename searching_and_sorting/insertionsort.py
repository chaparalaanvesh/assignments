"""Insertion sorting technique"""


def insertion_sort ( items ) :

    size = len(items)
    for i in range( 1 ,  size) :
        j = i
        while j > 0 :
            if items[ j -1 ] > items[ j ] :
                items[ j -1], items[ j ] = items[ j ] , items [j -1]
            j = j -1
        print(items)

a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a)

