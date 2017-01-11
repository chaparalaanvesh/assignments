def anagram(a1,a2):
    l1 = list(a1)
    l2 = list(a2)

    l1.sort()
    l2.sort()

    position = 0
    found = True
    while position < len(l1) and found:
        if l1[position] == l2[position]:
            position = position + 1
        else:
            found = False
    return found

print anagram('python','typhon')
