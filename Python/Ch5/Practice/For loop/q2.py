# Search for a number x in this tuple using loop : (1,4,9,16,25,36,49,64,81,100)

num = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter x : "))
i = 0
for el in num : 
    if(el == x):
        print("Number found at ",i)
        break
    else:
        i += 1
else:
    print("Element not found ")