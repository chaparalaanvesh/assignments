def length(a):
    a=a.split()
    print len(a)

def wordcount(a):
    list =a.split()
    list1 = []
    list.sort()
    for i in list:
        if i not in list1:
            list1.append(i)
            print i,list.count(i)

def lettercount(a):
     for i in range(ord('a'),ord('z')):
        print chr(i),a.count(chr(i))


a = 'a to the four where supers i be the other four'
length(a)
print 'words'
wordcount(a)
print 'letters'
lettercount(a)

