# Write a recursive fuction to print all element in a list

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    else:
        print(list[idx])
        print_list(list,idx+1)

fruit = ["mango","apple","banana","papaya","litchi"]
print_list(fruit)

