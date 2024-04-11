# Write a recursive function to calculate the factorial a number.

def factorial(n):
    if(n < 2):
        return 1
    else:
        return n * factorial(n-1)
    

num = int(input("Enter number : "))

print(num,"! =",factorial(num))
