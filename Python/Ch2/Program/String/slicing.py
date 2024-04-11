"""
Slicing 

    Slicing is the method for accessing parts of string

    Slicing Syntax is 

        str[Strating_index : Ending_index]
            important note:- always endind_index isn't included. 
                             Sub_string contain Strating_index to (Ending_index-1)
        
        Now, 
        For posive slicing
            str[ : n] is same as str[0 : n]

            str[n : ] is same as str[n : len(str)]

        For Negative slicing
            str[ : -n] is same as str[-len(str) : n]

            str[-n : ] is same as str[-n : -1]



"""

# Positive Indexing Slicing
str = "APPLE"
print(str[1 : 4])  # PPL
print(str[  : 3])  #APP
print(str[2 :  ])  #PLE
print(str[3 : 2 ])  #b no output, as it doesn't satisfied


# Negative Indexing Slicing 
#   A   P   P   L   E
#  -5  -4  -3  -2  -1


print(str[-3 : -1])  # PL
print(str[-len(str)  : -3])   #AP
print(str[  : -3])   #AP
print(str[-2 :  ])   #LE