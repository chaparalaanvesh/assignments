"""Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n """
import os
import re

def sum_words(f):
    file = os.open('len_of_words.txt','r')
    words = re.findall('\w+', file.read())
    output = sum([len(word) for word in words]) / len(words)
    file.close()
    return output
print sum_words(f='len_of_words.txt')
