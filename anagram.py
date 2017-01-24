"""def anagram(a1, a2):
    for letter in a1:
        if letter not in a2:
            return True
    return False

print anagram('python','on')"""



def anagram_test(word,anagrams):
    for alt in anagrams:
        if word == sorted(alt):
            return alt

print anagram_test(word = sorted('spot'),anagrams = ["tops","pots","spot","stop"])
