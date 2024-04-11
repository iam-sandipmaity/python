set = {5,9,3,4,8,2,50}
# 1
set.add(10)  # adds an element 
print(set)   #{1, 2, 3, 4, 5, 8, 9, 10}

# 2
set.remove(5)    #Remove an element from the set
print(set)       #{1, 2, 3, 4, 8, 9, 10}

# 3
set.clear()    #empties the whole set
print(set)     #set()

# 4
set = {1,7,8,9,5,6.5,7,9,2}

# 5
set.pop()       # removes an random value
print(set)      #{2, 5, 6.5, 7, 8, 9}


# 
set1 = {1,2,3,4,5}
set2 = {3,6,5,7}

# 7
print(set1.union(set2))    # Combines both sets value and return an new set
# {1, 2, 3, 4, 5, 6, 7}

# 8
print(set1.intersection(set2))  # combines common values and returns new set
# {3, 5}

