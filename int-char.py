def prime(n):
    a=[]
    if n>0:
        for i in range(n):
            if i%2 == 0:
                a.append(i)
        print "output:",a
    else: print"invalid"
    num2word(a)           #passing to

n = input("enter number:")

def num2word(a):
    b = []
    l = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    for a in l:

        b.append(a)
    return b

prime(10)
num2words(10)



