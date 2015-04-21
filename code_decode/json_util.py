#!/usr/bin/python
#coding:utf-8

#http://docs.python.org/library/json.html

import json

#####   python            ######   json    #####
#       dict              ######   object
#       list tuple        ######   array 
#       str unicode       ######   string 
#       int, long, float  ######   number 
#       True              ######   true 
#       Flase             ######   false 
#       None              ######   null 

###########json_encode#################
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
json_str = json.dumps(obj) #like php json_encode
print json_str

#json.dumps(obj) params: sort_keys separators indent skipkeys

#sork_keys 排序功能使得存储的数据更加有利于观察，也使得对json输出的对象进行比较
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1, sort_keys=True)

d2 = json.dumps(data2)
d3 = json.dumps(data2, sort_keys=True)
print d1
print d2
print d3
print d1==d2
print d1==d3

#indent 参数是缩进的意思，它可以使得数据存储的格式变得更加优雅：
data1 = {'b':789, 'c':456, 'a':123}
d1 = json.dumps(data1, sort_keys=True, indent=4)
print repr(d1)
print d1

#skipkeys default false dumps方法存储dict对象时，key必须是str类型，如果出现了其他类型的话，那么会产生TypeError异常，如果开启该参数，设为True的话，则会比较优雅的过度 
data = {'b':789,'c':456,(1,2):123}
print json.dumps(data, skipkeys=True)
#print json.dumps(data)

#separator 参数可以起到这样的作用，该参数传递是一个元组，包含分割对象的字符串： 

###########json_decode#################
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
json_str = json.dumps(obj)  #like php json_encode
obj2 = json.loads(json_str) #like php json_decode 
print obj2


