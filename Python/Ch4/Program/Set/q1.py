# Figure out a way to store 9 and 9.0 as separate values in the set

values = {9,"9.0"}
print(values)

values1 = {
    ("float", 9.0) , 
    ("int", 9)
}
print(values1)