import random
Account_number = 0

def create_account():
    print "enter your details"
    Account_number = (random.randint(0,99))
    f = open(str(Account_number)+'.txt','w')
    name = raw_input("Enter your name: \n")
    street = raw_input("Door no,street name: \n")
    city = raw_input("city,zipcode: \n")
    phone = input("phone number: \n")
    balance = input('enter initial balance: \n')
    d= {'name':name,'street':street,'city':city,'phone':phone,'balance' : balance,'account_number' : Account_number}
    print 'Your account number is: ',Account_number
    f.write(str(d))
    f.close()

create_account()
