input_string = raw_input("enter input string: ")
output = []
count = 1
for i in range(1, len(input_string)):
    print i
    if input_string[i - 1] == input_string[i]:
        count = count + 1
    else:
        output.append(  input_string[i - 1] + "-" + str(count) )
        count = 1
output.append(input_string[i] + "-" + str(count))
print output

