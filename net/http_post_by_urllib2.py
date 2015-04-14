# 其中urllib2.urlopen支持：
# 1、urllib2.urlopen('http://www.python.org/')
# 2、urlopen(url, data=None)
# 3、urlopen(url, data=None, timeout=<object object>)

import urllib
import urllib2

test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
test_data_urlencode = urllib.urlencode(test_data)

requrl = "http://192.168.81.16/cgi-bin/python_test/test.py"
req = urllib2.Request(url = requrl, data =test_data_urlencode)
print req

res_data = urllib2.urlopen(req, timeout=15)
res = res_data.read()
print res



