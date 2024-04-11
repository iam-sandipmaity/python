
str = "i am Sandip Maity"
print(str)
print(str.endswith("aity")) # return true if endswith condition satisfies
print(str.capitalize())     #capitalise 1st char but don't return value. so main str will not change
print(str)
print(str.replace("am","was")) # Replace all occurence of old value with new value.Aslo it don't return value. so main str will not change 
print(str)
print(str.find("Maity"))  # return 1st index of occurrrence

print(str.count("a")) # Count the total occurence of substr in the string


"""
Output Screen

    i am Sandip Maity
    True
    I am sandip maity
    i am Sandip Maity
    i was Sandip Maity
    i am Sandip Maity
    12
    3
"""