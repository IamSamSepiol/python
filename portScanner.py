#!/bin/python3
import socket
from datetime import datetime as dt
import sys

if len(sys.argv) == 2:
    print(sys.argv)
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Please provide the IP Address")

print("-" * 50)
print("Started Scanning {}".format(target))
print(dt.now())
print("-" * 50)

try:
    for i in range (50 , 85):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,i))                      
            if result == 0:
                print("{} Port is open".format(i) )
            s.close()
except KeyboardInterrupt:
     print("\n Exiting Program")
     sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")        
    sys.exit()
except socket.error:
     print("Couldn't connect to server")
     sys.exit()


