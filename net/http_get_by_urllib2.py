# urllib2使用注意细节：
# 1 Proxy 的设置
# 2 Timeout 设置
# 3 在 HTTP Request 中加入特定的 Header
# 4 Redirect
# 5 Cookie
# 6 使用 HTTP 的 PUT 和 DELETE 方法
# 7 得到 HTTP 的返回码
# 8 Debug Log

#urllib2.urlopen 返回一个文件类对象，它提供了如下方法：
#read() , readline() , readlines()，fileno()和close() 这些方法的使用与文件对象完全一样。
#info()     返回一个httplib.HTTPMessage 对象，表示远程服务器返回的HTTP头信息。
#getcode()  返回Http状态码，如果是http请求，200表示请求成功完成;404表示网址未找到。
#geturl()   返回请求的url地址。


import urllib
import urllib2

url = "http://192.168.81.16/cgi-bin/python_test/test.py?ServiceCode=aaaa"
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res


