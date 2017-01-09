import sys


s_len = int(raw_input().strip())
s = raw_input().strip()
for i in s:
    print i
    if i[0] == i[1]:
        del i
    else:
        print i

