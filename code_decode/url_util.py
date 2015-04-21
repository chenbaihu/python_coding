#coding:utf-8
#/usr/bin/python


# urllib.quote(string[, safe])：           对字符串进行urlencode编码。参数 safe 指定了不需要编码的字符;
# urllib.unquote(string) ：                对字符串进行urlencode解码；
# urllib.quote_plus(string [ , safe ] ) ： 与 urllib.quote 类似，但这个方法用'+'来替换' '，而 quote 用'%20'来代替' '
# urllib.unquote_plus(string ) ：          对字符串进行解码；
# urllib.urlencode(query[, doseq])：       将dict或者包含两个元素的元组列表转换成url参数。例如 字典{'name': 'dark-bull', 'age': 200}将被转换为"name=dark-bull&age=200"
# urllib.pathname2url(path)：              将本地路径转换成 url 路径；
# urllib.url2pathname(path)：              将url路径转换成本地路径；

import urllib

####### urlencode  #########

data = {'a':"test_data", 'b':"中国"}
#print type(data)
print urllib.urlencode(data)

data = "k1=v1&k2=v2&k3=v3"
print urllib.quote(data)       #like php urlencode


####### urldecode ##########
data = "k1=v1&k2=v2&k3=v3"
d = urllib.quote(data)
print urllib.unquote(d)

data = {'a':"test_data", 'b':"中国"}
d = urllib.urlencode(data)
print urllib.unquote(d)



