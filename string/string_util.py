#http://blog.csdn.net/iloveyin/article/details/7857230

#!/usr/bin/local/python

#lower upper
str1 = "abewrwelrjfsnfbsnfyweuropwennvh========="
print str1.upper()
print str1.upper().lower()

#strlen
str1 = "aaa"
print len(str1)

#strcmp  strncmp
str1 = "aaa"
str2 = "bbb"
if cmp(str1, str2)!=0:
    print "not eq"

if cmp(str1[0:1], str2[0:1]):
    print "not eq"

#insert
str = "123789"
str = str[:3] + "456" + str[3:]
print str

#strcat
str1 = "123456"
str2 = "789"
print str1+str2

#strchr
str1 = "abewrwelrjfsnfbsnfyweuropwennvh========="
print str1.index('j')

#strstr
str2 = str1[str1.find("elr"):]
print str2

#reversal
print str1[::-1]

#fmt string
arg1 = "arg1"
arg2 = "arg2"
arg3 = "arg3" 
args = "%s_%s_%s_this_is_test" % (arg1, arg2, arg3)
print args

arg1 = "arg1"
arg2 = "arg2"
arg3 = ['7', '8', '9']
print "".join(arg3)
args = "%s_%s_%s_this_is_test" % (arg1, arg2, "".join(arg3))
print args

#string join
value = ['111', '222', '333', '444']
s = "___".join(value)
print s

import string
value = ['111', '222', '333', '444']
s = string.join(value, '+')
print s

l = [10 , 12, 13]
value = [chr(v) for v in l]
print repr(value)

#split 
value = "abc;efg;hijk;"
listv = value.split(";")
print listv
for i in listv:
    print i 

import string
value = "abc;efg;hijk;"
listv = string.split(value, ";")
print listv

#trim  (strip lstrip rstrip)
str = "   aaaa bbb ccc   "
print len(str)
str = str.strip()
print len(str)
print str

def trim(str, tstr=' '):
    return str.strip(tstr)


