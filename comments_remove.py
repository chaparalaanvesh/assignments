#def find(s):
    #for i in s:
        #if i == '/':
           #return s.index(i)
    #a = s[:40] + s[(62):]
    #s = s[:s.find('/')-1]
    #str1 = str[str.find('\n')]
    #s1 = s[:s.index('/')] + s[s.index('\n')+1:]
    #print s1
    #return str1

#print find('#include int main(int argc,char *argv){ // First line of code\n printf("Hello World!!! "); return 0; }
#include int main(int *argc,char **argv){ // First line of code\n printf("Hello World!!! "); return 0; }
#include int main(int *argc,char **argv){ /* First line of code Printing Hello World */ printf("Hello World!!! "); return 0; }# ','/')

#def cmnt():
    #T = raw_input('enter num:')
    #if T>0:
     #   s = raw_input()
      #  for i in s:
       #     if i in ['\n','/*','* /',';']:
        #        s1 = s[:s.index('/*')] + s[s.index('*/')+1:]
         #       return s1
    #else:
     #   return ' insufficient entry'

#print cmnt()


t =input()
print t
for each_case in range(t):
    code=raw_input()
    print code
    single_cmt=False
    double_cmt=False
    ans=''
    i=0
    while i<len(code):
        if code[i]=='/':
            i+=1
            if code[i]=='/':
                single_cmt=True
            elif code[i]=='*':
                double_cmt=True
        elif code[i]=='*':
            i+=1
            if code[i]=='/':
                i+=1
                double_cmt=False
        elif code[i]=='\\':
            i+=1
            if code[i]=='n':
                i+=1
                single_cmt=False
        if not single_cmt and not double_cmt:
            ans+=code[i]
        i+=1
    print ans
