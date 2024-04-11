"""
List Slicing:-

    Slicing is done in same way as well as String

    list_name[strating_idx : ending_idx]
        Here ending_idx does't includeed. effective sublist will be from (starting_list to (ending_list-1))

     Now, 
        For posive slicing
            str[ : n] is same as str[0 : n]

            str[n : ] is same as str[n : len(str)]

        For Negative slicing
            str[ : -n] is same as str[-len(str) : n]

            str[-n : ] is same as str[-n : -1]

"""


marks = [56,89,65,68,92]

#   56  89  65  68  92
#   0   1   2   3   4 (positive indexing)
#  -5  -4  -3  -2  -1 (negative indexing)

print(marks)                   # [56,89,65,68,92]

print(marks[1 : 4])            # [89, 65, 68]
print(marks[3 : ])             # [68, 92]
print(marks[4 : len(marks)])   # [92]
print(marks[  : 4])            # [56, 89, 65, 68]
print(marks[3 : 1])            # []

print(marks[-3 : -1])          # [65, 68]
print(marks[-1 : -3])          # []
print(marks[-4 :   ])          # [89, 65, 68, 92]
print(marks[   : -1])          # [56, 89, 65, 68]

