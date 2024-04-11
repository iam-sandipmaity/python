"""
input are mainly 3 type
    1> default input or String input
        var_name = input("Enter var data or string data : ")
    
    2> int input
        var_name = int(input("Enter var data : "))

    3> float input 
        var_name = float(input("Enter var data : "))

Actually by default python take string as input, we have to just type cast for int or float input

"""

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
price = float(input("Enter Price : "))

print(type(name))
print(type(age))
print(type(price))

print("Your Name is ",name, " And Your age is ",age,"\nYour price is ",price)