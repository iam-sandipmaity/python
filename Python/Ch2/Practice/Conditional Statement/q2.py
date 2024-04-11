# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

if((num1 >= num2) and (num1 >= num3)):
    print("Greatest number is : ",num1)
elif(num2 >= num3):
    print("Greatest number is : ",num2)
else:    
    print("Greatest number is : ",num3)