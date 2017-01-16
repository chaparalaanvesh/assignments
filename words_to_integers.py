"""Using for loop"""

def words_to_int():
    input = ["hello","anvesh","rakesh","nikhil"]
    result = []
    for i in input:
        result.append(len(i))
    return result

print words_to_int()


#using higher order functions map()

input = lambda word:len(word)
print map(input,['hello','anvesh','rakesh','nikhil'])


#list comprehensions

input = [len(a) for a in ['hello','anvesh','rakesh','nikhil'] ]
for i in input:
    print i
