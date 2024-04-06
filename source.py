#!/usr/bin/python
fdesc = open("file.txt","w")

for i in range(1,100):
    fdesc.write(str(i))

fdesc.close()

