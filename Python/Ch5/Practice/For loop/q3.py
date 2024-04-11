# WAP to find the factorial of first n numbers.

n = int(input("Enter n : "))
fact = 1

for el in range(1,n):
    fact *= el
print(n,"!"," = ",fact)