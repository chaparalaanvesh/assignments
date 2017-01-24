"""mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[int(-1/2)])


try:
 if '1' != 1:
  raise "firstError"
 else:
  print("firstError has not occured")
except "firstError":
 print("firstError has occured")

for i in range(1, 6):
 print i, i, i, i, i


for i in range(1, 6):
 print str(i) * 5

def myfunc():
 try:
  print('Monday')
 finally:
  print('Tuesday')
myfunc()

def test1(param):
 return str(param)

def test2(param):
 return str(2 * param)

result = test1(1) + test2(2)
print(result)

x = 1
print(++++x)

mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[:-1])

mylist=[1, 5, 9, int('0')]
print(sum(mylist))

ints = set([1,1,2,3,3,3,4])
print(len(ints))

import random
print(random.seed(3))


def test():
 try:
  return 1
 finally:
  return 2
result = test()
print(result)

def test1(param):
 return param

def test2(param):
 return param * 2

def test3(param):
 return param + 3

result = test1(test2(test3(1)))
print(result)"""


from thread import start_new_thread

threadId = 1

def factorial(n):
   global threadId
   if n < 1:   # base case
       print "%s: %d" % ("Thread", threadId )
       threadId += 1
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))

c = raw_input("Waiting for threads to return...\n")
