import sys
year = 2016
name = str(input("Enter name:"))
print name
age = input('Enter age:')
print age
if (int(str(age)) < 80):
    temp = 80-int(str(age))
    year = year + temp
    print "person will turn 80 at the year:",year
else:
    print "he is already 80 years old"
