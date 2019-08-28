from socket import *

HOST='10.0.2.15'

c = socket(AF_INET, SOCK_DGRAM)
print ('connecting....')
c.bind(('',0))
print("done")
cnt=0
while cnt < 10:
    cnt = cnt + 1
    data = 'go'
    if (cnt%5==0):
        data = 'stop'
    result = c.sendto(data.encode(),('15.164.99.163', 9999))
    print(result)
    #data, addr = c.recvfrom(65535)
c.close()
