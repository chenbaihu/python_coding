import os
import sys
import httplib

def http_get(host, port):
    url = "http://" + host + ":" + port + "/cgi-bin/python_test/test.py?ServiceCode=aaaa"
    conn = httplib.HTTPConnection("192.168.81.16")
    conn.request(method="GET", url=url) 
    response = conn.getresponse()
    res= response.read()
    print res

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "%s ip port" % sys.argv[0]
        sys.exit(1)

    http_get(sys.argv[1], sys.argv[2]);


