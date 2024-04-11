"""
Positive Indexing
  
    A   P   P   L   E
    0   1   2   3   4

Negative Indexing 


    A   P   P   L   E
   -5  -4  -3  -2  -1


We use negative indexing if we don't know string length.

"""

str = "APPLE"

print(str[0])   #A
print(str[1])   #P
print(str[2])   #P
print(str[3])   #L
print(str[4])   #E

print("\n")

print(str[-1])   #E
print(str[-2])   #L
print(str[-3])   #P
print(str[-4])   #P
print(str[-5])   #A