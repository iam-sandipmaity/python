"""
Conversion are 2 types 
    1> Type Conversion / Automatic Conversion
    2> Type Casting / Manual conversion

"""

#  1> Type Conversion / Automatic Conversion

a = 1
b = 4.25
sum = a+b 
print(sum)
# int + float = float
# 1 + 4.25 = 5.25 as float

# 2> Type Casting / Manual conversion

a = 1
b = "2"
c = int(b)
sum = a+c
print(sum)
# int(Str) = int
# int + int(Str) = int + int = int