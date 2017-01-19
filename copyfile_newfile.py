"""Write a program that given a text file will create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file)."""

def copyfile_newfile(f):
    old_file = open('C:\Python27\len_of_words.txt')
    new_file = open('C:\Python27\ newfile.txt', 'wt')
    for line, text in enumerate(old_file):
        new_file.write('%s %s' % (line + 1,text))
    old_file.close()
    new_file.close()

print "file copied successfully - check the path for result"
copyfile_newfile(f='C:\Python27\ newfile.txt')
