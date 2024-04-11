"""
Function in python :- 

    block of statements that performs a specific task.

Function definition :- 

    def func_name(parameters1,parameter2,...):
        # some Work
        return val    #not necessary

Function call :- 

    func_name(argument1,argument2,....)


    
Function are used to types 
    1-> Built-in Funcions  [print(),len(),type(),range()]
    2-> User defined funcion

    
User defined Fuction are mainly two types:
    1-> with parameter 
    2-> without parameter

"""

# With parameter and return statement

def sum(a,b):
    s = a + b
    return s
print(sum(2,9))

# With parameter and without return statement
def diff(x,y):
    d = x-y
    print(d)

diff(9,6)

# without parameter

def hello():
    print("hello World")

hello()