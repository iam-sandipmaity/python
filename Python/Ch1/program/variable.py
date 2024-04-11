# In python we don't have to pre difine any variable type. Python automatically detected it's type from it's value

""""
Some rules of Variable

    1. Variable can't start with any number
        Ex:- 1variable is invalid but variable1 is valid
    2. Variable can't hold any special charecter init except "_"
        Ex:- my$Variable is invalid but my_Variable is valid
    3. Variable length could be any length
        Ex:- my_variable_of_this_function
    4. variable name can start with "_"
        Ex:- _var is valid variable name
"""

name = "Sandip"   #String
age = 20          #Int
_price = 66.94    #Float
print(name)
print(age)
print(_price)
print(type(name))
print(type(age))
print(type(_price))