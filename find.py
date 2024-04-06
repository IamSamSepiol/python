#!/usr/bin/python

import os

for i in os.listdir("."):
    if os.path.isfile(i):
        print(i + "  is a file")
    elif os.path.isdir(i):
        print(i + " is a directory")


