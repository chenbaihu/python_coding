#import struct
#pack、unpack、pack_into、unpack_from
#https://docs.python.org/2/library/struct.html#module-struct

from struct import pack

def create_req():
    req_body  = ""
    req_body += "a=b&c=d&e=f"
    req_body += "\r\n"
    ext = "ext=ext:1,test||abc:1,abc||\r\n";
    body += ext;  #urldecode($extinfo);
    
    header = [20, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    req    = "".join([chr(i) for i in header])+req_body;
    #print repr(req[:2])
    #print repr(req[6:8])
    #print repr(req[10:])
    
    req    = req[:2] + pack('!h', len(body)) + pack('!h', 100) + req[6:8] + pack('!h', 0) + req[10:]
    return req


