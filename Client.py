#!/usr/bin/python
#*-* coding: utf-8 *-*
from socket import *

HOST='203.255.176.80'

c = socket(AF_INET, SOCK_STREAM)
print 'connecting....'
c.connect((HOST,12000))
print 'ok'
cnt=0
while 1:
	cnt++
	if (cnt%50==0):
		data = 'stop'
	else:
		data = 'go'
        if data:
                c.send(data)
        else:
                continue
c.close()
