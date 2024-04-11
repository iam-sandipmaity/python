"""
Using the os module .
module (like a code library) is a file written by another programmer that generally has a functions we can use.

import os
os.remove(filename)

"""
with open("first.txt","w") as f:
    f.write("new data")

import os
os.remove("first.txt")


