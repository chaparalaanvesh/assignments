import os
import sys

def parse_file(path):

    fd = open('newfile.txt','r')
    i = 0
    spaces = 0
    tabs = 0

    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    fd.close()

    return spaces,tabs,i+1

parse_file('C:\Python27\newfile.txt')
