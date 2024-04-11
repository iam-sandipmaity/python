"""
SET

    Set is the collection of unordered items. Each element in the set must be uniqe and immutable.

    set 
        -> null_set = set()  empty set syntax
        -> each data unique
            Ex :- 
                nums = {1,2,3,4,2,1,3,5}
                print(nums) -> {1,2,3,4,5}
                
        -> set is mutable
        -> each data is immutable

        -> we can add, remove elements in the set. So, set is mutable.
        but, we can't change any elements value. So, Set's elements are immutable

        -> int, float, string , tuple all data type can stored in Set. 
        But, list and Dictionary can't stored in the set
"""

# Creating empty set
empty_set = set()
empty_set1 = {}  # it will create a empty dictionary
print(type(empty_set))  # <class 'set'>
print(type(empty_set1)) # <class 'dict'>

# Set is uniqe in value
num = {1,5,3,2,1,2,3}
print(num)
print(type(num))

# set can hold int, float, string, tuple but can't list and dictionary

set1 = {1,2,3.5,"Sandip", (2,9.55,"Maity")}
print(set1)         #{1, 2, 3.5, (2, 9.55, 'Maity'), 'Sandip'}
print(type(set1))   #<class 'set'>


"""
set2 = {["Sandip","Maity",5,9,8.6],}       
print(set2)        #unhashable type: 'list' and send error

set3 = {{"Name" : "Sandip", "age" : 20}}
print(set3)         #TypeError: unhashable type: 'dict'
"""

# We can add or remove value at set so, set is mutable
set = {1,5,3}
set.add(4)
print(set)   #{1, 3, 4, 5}

set.remove(1)
print(set)   #{3, 4, 5}

# Set each element is immutable

set_data = {1,2,3}

# set_data[1] = 5  #TypeError: 'set' object does not support item assignment