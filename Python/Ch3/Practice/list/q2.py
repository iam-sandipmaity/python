# Write a program to check if a list contains a palindrome of elements.


list = []
n = int(input("Enter n : "))
i = 0
while i < n :
    list.append(int(input("Enter Element : ")))
    i += 1

print(list)

copy_list = list.copy()

# print(copy_list)
# print(list)

copy_list.reverse()

# print(copy_list)
# print(list)

if(copy_list == list):
    print("Palindromic")
else:
    print("Not Palindromic")

