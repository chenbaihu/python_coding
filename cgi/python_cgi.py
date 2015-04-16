#修改.htaccess文件，让Apache能够识别py文件为CGI脚本程序:
#AddType text/html py  AddHandler cgi-script .py

#使用Python自带的cgi库，可以很容易的实现CGI编程。
#下面的例子实现了使用类FieldStorage得到POST或GET参数的方法

#表单示例:
#<form method="POST" action="/cgi-bin/test.py">
#    <p>Your first name: <input type="text" name="firstname">
#    <p>Your last name: <input type="text" name="lastname">
#    <p>Click here to submit form: <input type="submit" value="Yeah!">
#    <input type="hidden" name="session" value="1f9a2">
#</form>

#这里的/cgi-bin/表示调用CGI，在apche的配置文件conf/httpd.conf中配置了/cgi-bin/的路径

#!/usr/local/bin/python

import cgi
def main():
    print "Content-type: text/html\n"      
    form = cgi.FieldStorage()   # parse query      
    if form.has_key("firstname") and form["firstname"].value != "":
        print "<h1>Hello", form["firstname"].value, "</h1>"      
    else:
        print "<h1>Error! Please enter first name.</h1>" 

main()

