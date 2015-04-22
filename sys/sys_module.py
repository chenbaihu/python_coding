#!/usr/bin/python
#coding:utf-8

import sys
import getopt

#sys.path    查找模块所在目录的目录名列表，如果模块在其它路径下，可以使用sys.path.append(路径)。

for i in sys.path:
    print  i

#sys.modules 方法可以将模块的名字映射到实际存在的模块上，它只应用于目前导入的模块，类型为dict，key为模块名，value为该模块的路径。
for i in sys.modules:
    print i
    print sys.modules[i]

#args
print sys.argv

#getopt
#python ./sys_module.py --host "aaaaa" -d "bbbbb" -h -v --data_file "./test" --proto "HTTP" --req_type "tttt"
opts, args = getopt.getopt(
        sys.argv[1:],
        "d:hv",
        [ "host=", "data_file=", 'req_type=', 'proto=']
        )
opts_dict = dict(opts)

print opts_dict
#print args

#sys.setdefaultencoding('utf-8')
