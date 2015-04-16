import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = raw_input()
    if not msg:
        break 
    s.sendto(msg, address)
    data,addr = s.recvfrom(1024)
    print 'recv rsp[ ',data,' ]addr[ ',addr,' ]'
    s.close()

