"""
Range():-

    Range() functions returns a sequence of numbers staring from 0 (by default), and increments by 1 (by default) and stops before a specific number 

    range(start? , stop , step? )
            ^               ^
            |               |
      by default 0     by default 1



"""


for el in range(5):
    print(el)

"""
0
1
2
3
4
"""
print("\n")
for el in range(2,5):
    print(el)

"""
2
3
4
"""
print("\n")
for el in range(2,10,2):
    print(el)

"""
2
4
6
8
"""