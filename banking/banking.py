import create_account
import display_account
import deposit_withdrawl
print 'welcome to banking services: '
print '1: Create Account'
print '2: Balance Enquiry'
print '3: Cash Withdrawl'
print '4: Deposits'
print '5: Delete Account'
choice = input("enter your choice(1/2/3/4/5): ")

if choice == 1:
    create_account.create_account()

if choice == 3:
    deposit_withdrawl.deposit(self,100)

if choice == 4:
    deposit_withdrawl.withdrawl(self,50)

if choice == 5:
    account_number = input("enter account number: ")
    display_account.customers(account_number)




