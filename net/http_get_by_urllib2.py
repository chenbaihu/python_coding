# urllib2ʹ��ע��ϸ�ڣ�
# 1 Proxy ������
# 2 Timeout ����
# 3 �� HTTP Request �м����ض��� Header
# 4 Redirect
# 5 Cookie
# 6 ʹ�� HTTP �� PUT �� DELETE ����
# 7 �õ� HTTP �ķ�����
# 8 Debug Log

#urllib2.urlopen ����һ���ļ���������ṩ�����·�����
#read() , readline() , readlines()��fileno()��close() ��Щ������ʹ�����ļ�������ȫһ����
#info()     ����һ��httplib.HTTPMessage ���󣬱�ʾԶ�̷��������ص�HTTPͷ��Ϣ��
#getcode()  ����Http״̬�룬�����http����200��ʾ����ɹ����;404��ʾ��ַδ�ҵ���
#geturl()   ���������url��ַ��


import urllib
import urllib2

url = "http://192.168.81.16/cgi-bin/python_test/test.py?ServiceCode=aaaa"
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res


