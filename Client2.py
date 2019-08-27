#!/usr/bin/python
#*-* coding: utf-8 *-*
from socket import *

HOST='10.0.2.255'

c = socket(AF_INET, SOCK_DGRAM)
print ('connecting....')
c.connect((HOST,12000))
print ('ok')
cnt=0
while 1:
    print("while")
    cnt+=1
    if (cnt%50==0):
        data = 'stop'
    else:
        data = 'go'
    if data:
        print(data)
        data = str.encode(data)
        c.send(data)
        print("send data")
    else:
        continue
c.close()
