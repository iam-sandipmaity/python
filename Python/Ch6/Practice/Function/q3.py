# WAF to find the factorial of n.

def factorial(n):
    fact = 1
    for el in range(1,n+1):
        fact *= el
        
    return fact


num = int(input("Enter number : "))
print(num,"! = ",factorial(num))