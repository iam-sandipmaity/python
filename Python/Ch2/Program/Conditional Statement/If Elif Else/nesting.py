"""
if(condition):          
    if(condition):    
    
this type of statement iks called nated if and it is called nesting
"""

# WAP using nesting if for 18 to 60 years can drive car

age = int(input("Enter Your Age : "))
# nesting
if(age >= 18):
    if(age <= 60):
        print("You can drive")
    else:
        print("Your age is higher than 60, So you can't drive")

else: 
    print("You are an adult. So you can't drive")
