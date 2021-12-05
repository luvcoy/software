import os
import sys

filepath = sys.argv[1]
file = open(filepath, 'rb')
save = open(filepath + "_dump", 'w')
size = os.path.getsize(filepath)
for i in range(1, size + 1):
    save.write("0x" + file.read(1).hex())
    if i % 16 == 0:
        save.write("\n")
    else:
        save.write(",")
file.close()
save.close()
