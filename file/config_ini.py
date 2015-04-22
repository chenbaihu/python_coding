import ConfigParser
#coding:utf-8

#config.ini
#[data1]
#key1=value1
#key2=value2
#
#[data2]
#key3=value3
#key4=value4

config = ConfigParser.ConfigParser() #初始化config实例（建立一个空的数据集实例）

#config.read(filename)               #通过load文件filename来初始化config实例
config.read("./config.ini")

#config.get(section, key)            #获得指定section中的key的value
value1 = config.get("data1", "key1")
print value1

#config.set(section, key, value)      #在指定section中，添加一对key-value键值对
config.set('data1', 'key1', "value11111")
value1 = config.get("data1", "key1")
print value1

#config.remove_option(section, key)   #删除指定section的key
config.remove_option('data1', 'key1')

#config.remove_section(section)       #删除指定section
config.remove_section('data1')

#config.write(open(filename, 'w'))    #保存配置
config.write(open('config_tmp.ini', 'w'))

