""""
Data Types

    There are mainly 5 type of data is available.
        1> Integer (+ve, -ve, 0)
        2> String  

            String could be define in 3 ways.
                a> within '' . like 'Hello World'
                b> within "" . like "Hello World"
                c> within ''' ''' . like '''Hello World'''

                    Why their are 3 ways to difine String
                    
                        ANS :-  There are 3 ways to define string because we may use single quote or double quote in our String so for this flexibility we have 3 different ways.

        3> Float (Decimal value)
        4> Boolean (True , False)
        5> None (no value)

"""

age = 20
name1 = 'Sandip'
name2 = "Sandip"
name3 = '''Sandip'''
price = 22.56
isRain = False
isSunday = True
empty_val = None

print(age , "  " , type(age))
print(name1 , "  " , type(name1))
print(name2 , "  " , type(name2))
print(name3 , "  " , type(name3))
print(price , "  " , type(price))
print(isRain , "  " , type(isRain))
print(isSunday ,"  " , type(isSunday))
print(empty_val , "  " , type(empty_val))


""""
output screen 

    20    <class 'int'>
    Sandip    <class 'str'>
    Sandip    <class 'str'>
    Sandip    <class 'str'>
    22.56    <class 'float'>
    False    <class 'bool'>
    True    <class 'bool'>
    None    <class 'NoneType'>
    
"""