import sys
input = raw_input('enter input: ')
output = []
for i in input:
    if type(i) == str:
        output.append(i)
output=''.join(output)
print output