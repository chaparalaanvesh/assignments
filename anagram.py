def anagram(a1, a2):
    if len(a1) != len(a2):
        return False
    for letter in a1:
        if letter not in a2:
            return False
    return True

print anagram('python','typhon')
