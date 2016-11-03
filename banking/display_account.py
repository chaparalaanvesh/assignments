import os

def customers(account_number):
    for details in os.listdir("C:\\Python27\\assignments\\banking"):
        if details.endswith(".txt"):

            information(details,account_number)

def information(details,account_number):
    os.chdir('C:\\Python27\\assignments\\banking')

    f = open(details,'r')

    a= f.read()
    b = eval(a)
    for i in b:
        print i
        print type(i)
        print i['balance']
customers(account_number)

