"""
Tuple 

    A buit-in data type that lets us to create immutable sequence of values...

            list     -> mutable
    tuple and String -> immutable

    tuple are written in between parent thesis
    tup = (45,98,35,96)

    same as list and Strig we can easily acseess any data what ever we need using indexing...
    print(tup[0])   will give 45 as output
    print(tup[3])   will give 96 as output

    but, as tuple is immutable, so 
                tup[0] = 43    value assigning isn't possible

    some basics of tuple
        1> Empty tuple  ->  tup()
        2> single value tuple -> tup(val,)
                    example:- tup(6,)

                    It's vary important to provide this "," after value in case of single value tuple, othewise it consider it as a integer or float or string
        3> more than 1 value tup -> 
                -> tup(v1,v2,v3,) or tup(v1,v2,v3)
                tup(1,2,3,) or tup(1,2,3)

    
Slicing in tuple:

    Also slicing is possible in tuple asc well as string or list
Tuple function:-
    some important functions are 

        -> tup.index(el)  returns index of first occuence at the tuple
                ex:- tup = (2,1,8,3,1)
                    tup.index(1) is 1

        -> tup.count(el)  counts total occurence of the element from the tuple
                ex:- tup = (2,1,8,3,1)
                    tup.index(1) is 2
"""

tup_int = (6)
tup_float = (6.35)
tup_str = ("Sandip")

print(type(tup_int))        #<class 'int'>
print(type(tup_float))      #<class 'float'>
print(type(tup_str))        #<class 'str'>

null_tup = ()
print(null_tup)             #()
print(type(null_tup))       #<class 'tuple'>

single_tup_int = (5,)
single_tup_float = (9.6,)
single_tup_str = ("Sandip",)
print(single_tup_int)
print(single_tup_float)
print(single_tup_str)

tup = (1,6,8)
tup1 = (1,8,9,)
print(type(tup))
print(type(tup1))

print(tup)
print(tup1)

#  Tuple Slicing
print("Tupple Slicing ")
tup = (1,9,3,8,2)

print(tup[1:3])
print(tup[ : 3])
print(tup[3 : ])

# Tuple function
print("Tupple Function")
tup = (1,2,3,1)
print(tup.index(1))
print(tup.count(1))



"""
Total Output Screen 

<class 'int'>
<class 'float'>
<class 'str'>
()
<class 'tuple'>
(5,)
(9.6,)
('Sandip',)
<class 'tuple'>
<class 'tuple'>
(1, 6, 8)
(1, 8, 9)
Tupple Slicing
(9, 3)
(1, 9, 3)
(8, 2)
Tupple Function
0
2

"""