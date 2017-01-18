"""Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n """

import re

def sum_words(f):
    file = open('C:\Python27\len_of_words.txt')
    words = re.findall('\w+', file.read())
    output = sum([len(word) for word in words]) / len(words)
    return output
    file.close()

print sum_words(f='C:\Python27\len_of_words.txt')
