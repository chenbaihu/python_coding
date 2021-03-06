#!/usr/bin/python
#coding:utf-8

import glob
import os

l = glob.glob("*.py");
print l

#将文件的内容读入列表，相当于php的file：
f = file("./datetime_util.py", "r");
for line in f.readlines():
    print line

fobj = open("test.txt", "r")
for line in fobj:
    print line

fobj.close()

#关于open 模式：
#w      以写方式打开，
#a      以追加模式打开 (从 EOF 开始, 必要时创建新文件)
#r+     以读写模式打开
#w+     以读写模式打开 (参见 w )
#a+     以读写模式打开 (参见 a )
#rb     以二进制读模式打开
#wb     以二进制写模式打开 (参见 w )
#ab     以二进制追加模式打开 (参见 a )
#rb+    以二进制读写模式打开 (参见 r+ )
#wb+    以二进制读写模式打开 (参见 w+ )
#ab+    以二进制读写模式打开 (参见 a+ )

os.remove("test_tmp.txt");      #
os.mknod("test_tmp.txt")        #创建空文件

fobj = open("test.txt", "r")
line = fobj.readline(1024)
print "line=%s" % line
fobj.close()

fobj.read([size])           #size为读取的长度，以byte为单位

fobj.readline([size])       #读一行，如果定义了size，有可能返回的只是一行的一部分

fobj.readlines([size])      #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。
                            #如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。

fobj.write(str)             #把str写到文件中，write()并不会在str后加上一个换行符

fobj.writelines(seq)        #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。

fobj.close()                #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。  
                            #如果一个文件在关闭后还对其进行操作会产生ValueError

fobj.flush()                #把缓冲区的内容写入硬盘

fobj.fileno()               #返回一个长整型的”文件标签“

fobj.isatty()               #文件是否是一个终端设备文件（unix系统中的）

fobj.tell()                 #返回文件操作标记的当前位置，以文件的开头为原点

fobj.next()                 #返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就
                            #是调用next()函数来实现遍历的。

fobj.seek(offset[,whence])  #将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。
                            #但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。
                            #2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，
                            #文件操作标记会自动返回到文件末尾。

fobj.truncate([size])       #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
                            #如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，
                            #也可能是以一些随机的内容加上去。

os.mkdir("file")            #创建目录

shutil.copyfile("oldfile","newfile") #oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")     #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
shutil.copytree("olddir","newdir")   #olddir和newdir都只能是目录，且newdir必须不存在

shutil.move("oldpos","newpos")       #移动文件（目录）

os.rename("oldname","newname")       #文件或目录都是使用这条命令

os.remove("file")                    #删除文件

os.rmdir("dir")              #只能删除空目录
shutil.rmtree("dir")         #空目录、有内容的目录都可以删

os.chdir("path")             #转换目录

os.getcwd()                  #函数得到当前工作目录，即当前Python脚本工作的目录路径。
os.listdir(dirname)          #返回指定目录下的所有文件和目录名。

os.path.split()              #函数返回一个路径的目录名和文件名。
#例如：
#os.path.split('/home/swaroop/byte/code/poem.txt')
#('/home/swaroop/byte/code', 'poem.txt')
os.path.splitext()           #分离文件名与扩展名 

#函数分别检验给出的路径是一个文件还是目录
os.path.isdir(name)          #判断name是不是一个目录，name不是目录就返回false 
os.path.isfile(name)         #判断name是不是一个文件，不存在name也返回false 
os.path.exists(name)         #判断是否存在文件或目录name 

os.path.getsize(name)        #获得文件大小，如果name是目录返回0L 
os.path.abspath(name)        #获得绝对路径 
os.path.normpath(path)       #规范path字符串形式 
os.path.join(path, name)     #连接目录与文件名或目录 
os.path.basename(path)       #返回文件名 
os.path.dirname(path)        #返回文件路径

os.name                      #字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.linesep                   #字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
os.system()                  #函数用来运行shell命令。
os.getenv()                  #函数分别用来读取和设置环境变量。
os.putenv()                 
os.umask(mask)               #设置当前文件权限掩码，并返回上一个权限掩码。
os.setsid()                  #使独立于终端的进程（不响应sigint，sighup等），使脱离终端。




