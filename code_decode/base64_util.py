#import base64
#base64的8个方法（encode, decode, encodestring, decodestring, b64encode,b64decode, urlsafe_b64decode,urlsafe_b64encode）
#encodestring 和 decodestring     用来编码和解码字符串
#b64encode    和 b64decode        用来编码和解码字符串，并且有一个替换符号字符的功能。
#                                 这个功能是这样的：因为base64编码后的字符除了英文字母和数字外还有三个字符 + / =, 
#                                 其中=只是为了补全编码后的字符数为4的整数，而+和/在一些情况下需要被替换的，b64encode和b64decode正是提供了这样的功能。
#                                 至于什么情况下+和/需要被替换，最常见的就是对url进行base64编码的时候。
#urlsafe_b64encode 和urlsafe_b64decode     这个就是用来专门对url进行base64编解码的，实际上也是调用的前一组函数(即：b64encode和b64decode)。
#https://docs.python.org/2/library/base64.html

#!/usr/local/bin/python 

import base64

filea = open(r'./1.txt','r')
lines = filea.readlines()
writefile=open(r'./2.txt','w')

for i in lines:
    word = i.strip()
    b = base64.decodestring(word)
    print b
    writefile.write(b)
    writefile.write('\n')

writefile.close()
filea.close()

