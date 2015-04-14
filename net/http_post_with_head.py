# coding: utf-8

import random
import urllib
import urllib2
import httplib
import socket
import string 

import os
import sys
import binascii
import base64
import struct
from struct import pack

def http_post_with_http_header(host, port, url, reqstr, header):
    conn = httplib.HTTPConnection(host, port)
    conn.request("POST", url, reqstr, header)  
    response = conn.getresponse()
    res      = response.read()
    print response.getheaders()		// http头
    conn.close()
    return res

def create_req():
    body  = ""
    body += "key1=value1&key2=value2&key3=value3"
    ext = "ext=ext";
    body += ext;  #urldecode($extinfo);

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "%s ip port" % sys.argv[0]
        sys.exit(1)

    url = 'http://%s:%s/test.php' % (sys.argv[1], sys.argv[2]);
	
	req = create_req();
	
	extra_str=base64.b64encode("a=a1&b=b1&c=c1");
	req_http_header = {"extra":extra_str};
	respd = http_post_with_http_header(sys.argv[1], sys.argv[2], url, req, req_http_header);
	