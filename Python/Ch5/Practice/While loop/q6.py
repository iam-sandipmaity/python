# WAP to find the sum of first n numbers. (using while)

sum,i = 0,0
n = int(input("Enter n : "))

while (i <= n) : 
    sum += i
    i += 1
  
print(sum)