# WAP to print all the even aand odd numbers of first n numbers by using Continue 

n = int(input("Enter n : "))

i = 1


print("ODD NUMBERS : \n")
while(i <= n):
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1

i = 1
print("\nEVEN NUMBERS : \n")
while(i <= n):
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1