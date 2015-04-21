#!/usr/bin/python

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

#sork_keys
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

#indent
data1 = {'b':789, 'c':456, 'a':123}
d1 = json.dumps(data1, sort_keys=True, indent=4)
print repr(d1)
print d1

#skipkeys default false 
data = {'b':789,'c':456,(1,2):123}
print json.dumps(data, skipkeys=True)
#print json.dumps(data)

#separator 


###########json_decode#################
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
json_str = json.dumps(obj)  #like php json_encode
obj2 = json.loads(json_str) #like php json_decode 
print obj2


