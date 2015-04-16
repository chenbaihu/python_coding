#!/usr/bin/python

import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.16.29.69',2000))  
data=s.recv(512)
print 'the data received is\n    ',data
s.send('hihi I am client')

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect(('10.16.29.69',2000))
data2=sock2.recv(512)
print 'the data received from server is\n   ',data2
sock2.send('client send use sock2')
sock2.close()

s.close()

