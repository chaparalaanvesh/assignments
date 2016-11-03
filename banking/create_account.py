import random
def create_account():
    Account_number = (random.randint(0,9))
    f = open(str(Account_number)+'.txt','w')
    d = {}
    name = raw_input("Enter your name: \n")
    address1 = raw_input("Door no,street name: \n")
    address2 = raw_input("city,zipcode: \n")
    phone = input("phone number: \n")
    balance = input('enter initial balance: \n')
    d= {'name':name,'address1':address1,'address2':address2,'phone':phone,'balance' : balance,'account_number' : Account_number}
    print 'Your account number is: ',Account_number
    f.write(str(d))
    f.close()

