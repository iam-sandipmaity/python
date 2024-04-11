"""
File I/O in Python

    pyhton can be used to perform operation on a file.(read & write data)

    Types of all files 
        1-> Text files : .txt, .docx, .log etc
        2-> Binary files : .mp4, .mov, .png, .jpeg etc


    
"""

"""
# Open file


f = open("file_name","mode")
data = f.read()
f.close()



reading a file:

data = f.read()         #reads the entire file
data = f.read(n)        #reads the first n charecter of the file
data = f.readline()     #reads one line at a time

"""

# Open file
f = open("sample.txt","r")
data1 = f.read()
data2 = f.read(5)
data3 = f.readline()

print(data1)


print(type(data1))
f.close()


"""
Character	Meaning
'r'	        open for reading (default)
'w'	        open for writing, truncating the file first
'x'	        create a new file and open it for writing
'a'	        open for writing, appending to the end of the file if it exists
'b'	        binary mode
't'	        text mode (default)
'+'	        open a disk file for updating (reading and writing)


r+  read + overwrite    pointer -> start    no truncate
w+  read + overwrite    pointer -> start    truncate (all data deleted)
a+  read + append       pointer -> end      no truncate 




"""






"""



Writing to a file

    f = open("demo.txt","w")
    f.write("This is a new line") # overwrite the entire file

    f = open("demo.txt","a")
    f.write("This is a new line") # adds to the file

    
"""

# Writting to a file

f = open("demo.txt","w+")
f.write("This is a new line ")


f = open("demo.txt","a+")
f.write("Hi How are you")





