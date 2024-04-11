# Search for a number x in this tuple using loop : (1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)

n = int(input("Enter n : "))
res = 0
i = 0
while(i < len(tup)):
    if(tup[i] == n):
        print("Found at index : ",i)
        res = 1
        break
    i += 1

if (res != 1):
    print("Element not found")