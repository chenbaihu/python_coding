#!/usr/bin/python
#coding:utf-8

import time
import datetime

#获取当前系统时间:
now = time.time()
print now

now = time.localtime()
print now

date_time = str(now.tm_year) + '-' + str(now.tm_mon) + '-' + str(now.tm_mday) + ' ' + str(now.tm_hour) + ':' + str(now.tm_min) + ':' + str(now.tm_sec)
print date_time

date = "%4d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
print date

date_time = "%4d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
print date_time

#获取当前系统时间，并转换成字符串类型：
cur_time = time.strftime("%Y-%m-%d %X", time.localtime(time.time()))
print cur_time

#获取当前系统日期:
now = time.localtime()
now_date = datetime.datetime(now[0], now[1], now[2])
print now_date
print now_date.strftime("%Y-%m-%d") 

print datetime.datetime.now()

d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(days =10)
print str(d3)
print "ctime=%s" % d3.strftime("%Y-%m-%d %02d:%02d:%02d")
d4 = d1 + datetime.timedelta(seconds =100)
print "ctime=%s" % d4.strftime("%Y-%m-%d %02d:%02d:%02d")


#计算给定时间delta天后或delta天前的时间：
base_time="20121012" #转换成2012-10-12
delta=3              #计算3天后的日期，如果是delta=-3，计算3天前的日期
d1 = datetime.datetime(int(base_time[0:4]), int(base_time[4:6]), int(base_time[6:8])) 
d2 = d1 + datetime.timedelta(days = delta)
print d2
print d2.strftime("%Y-%m-%d") 

#计算两个日期之间的时间查:
d1 = datetime.datetime(2004, 12, 30)
d2 = datetime.datetime(2004, 12, 29)
print (d1 - d2).days    #两个日期相差的天数

#字符串转换成时间 string -> time 和 time  -> string  和 string -> datetime 和 datetime -> string
date = "2012-04-05"
date = time.strptime(date, "%Y-%m-%d")  #string -> time 
print type(date) #struct_time
    
date = time.strftime("%Y-%m-%d", date)  #time -> string
print type(date) #str


date = "2012-04-05"
date = datetime.datetime.strptime(date, "%Y-%m-%d")  #string   -> datetime
print type(date) #datetime.datetime
print date

date = date.strftime("%Y-%m-%d")            #datetime -> string
print type(date) #str
print date


date = "2012-04-05"
date = time.strptime(date, "%Y-%m-%d")               #string -> time
date = datetime.datetime(date[0], date[1], date[2])  #time -> datetime
print type(date) #datetime.datetime



