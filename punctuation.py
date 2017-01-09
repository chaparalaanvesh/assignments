# A program to print the count and occourance of the punctuation marks in the string




def punctuation_occourance():
    input_str = raw_input('enter string: ')
    punctuation = [',','.','/',';',':','"','\ ',"'"]
    count = 0
    #for i in input_str:
        #if i in punctuation:
            #count = count + 1
    #return count
    a = {}
    for j in input_str:
        if j in punctuation:
            a[j]= 1
            count = count +1
    #else:
        #a[j] = a[j] +1
    return a,count




print punctuation_occourance()





