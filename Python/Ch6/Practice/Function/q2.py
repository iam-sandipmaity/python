# WAF to print the elements of a list in a single line.(list is the parameter)


num = [1,6,5,9,8,4]
city = ["Kolkata","Delhi","Mumbai","Chennai","Banglore","Hydrabad"]
# print(num)
# print(city)

def print_list(list):
    for el in list:
        print(el,end = " ")
    print()

print_list(num)
print_list(city)