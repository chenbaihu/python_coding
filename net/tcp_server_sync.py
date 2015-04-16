#!/usr/bin/python

import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.16.29.69', 2000))
s.listen(5)

while True:
    cs,address = s.accept()
    print 'got connected from',address
    cs.send('hello I am server,welcome')
    ra=cs.recv(512)
    print ra
    cs.close()
