//////////// Server.cpp /////////////
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<iostream>
using namespace std;
 
#define BUFSIZE 512
 
int main()
{
 int sock=socket(AF_INET, SOCK_DGRAM, 0);
 int retval;
 
 sockaddr_in serveraddr;
 bzero(&serveraddr, sizeof(serveraddr));
 serveraddr.sin_family=AF_INET;
 serveraddr.sin_port=htons(9999);
 serveraddr.sin_addr.s_addr=htonl(INADDR_ANY);
 retval=bind(sock, (sockaddr*)&serveraddr, sizeof(serveraddr));
 
 sockaddr_in clientaddr;
 int addrlen;
 char buf[BUFSIZE+1];
 
 while(1)
{ 
  addrlen=sizeof(clientaddr);
  retval=recvfrom(sock,buf,BUFSIZE,0,(sockaddr*)&clientaddr,
                       (socklen_t*)&addrlen);
 
  buf[retval]='\0';
  cout<<"[UDP/"<<inet_ntoa(clientaddr.sin_addr)<<":"
        <<ntohs(clientaddr.sin_port)<<"] "<<buf<<endl; 
 }
 
 close(sock);
 return 0;
}
