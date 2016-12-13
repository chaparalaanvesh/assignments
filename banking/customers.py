import os


def customers():
    Account_number = raw_input("enter account number: ")
    for details in os.listdir("C:\\Python27\\assignments\\banking"):
        if details.endswith(".txt"):
            f =open(details,'r')



