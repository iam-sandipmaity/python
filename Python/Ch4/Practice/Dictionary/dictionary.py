"""
Dictionary :-

    ->Dictionary are used to store data values in KEY:VALUE pair

    ->They are unordered, mutable (changable) & don't allow to duplicate keys

    ->Here key is acted as index and we can easily acseess any "values" by thier "key" values.

"""


student = {
    "first_name" : "Sandip",
    "last_name"  : "Maity", 
    "age"        : 20,
    "Education"  : "B.Tech",
    "salary"     : 5.35
}

print(student)
print(type(student))

print("Hello ",student["first_name"],student["last_name"],". You are",student["age"], "years old. You are currently study in",student["Education"], "and your pocket money is",student["salary"])


# We could easily assign new value to any key 

print(student["first_name"])
student["first_name"] = "Rupam"
print(student["first_name"])

student["first_name"] = "Pradip"
print(student["first_name"])

