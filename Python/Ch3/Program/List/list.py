"""
List in Python

    List is a built in data type in python that stores set of values.

    list can store 
        Integer, float,String etc...

    Example:-
        student = ["Sandip" , 85, "Maity",12.65] 

            From this list we can access every element of the list using their index number
                print(student[0]) will print "Sandip"
                print(student[1]) will print 85
                .......

            Also, list is mutable. So,
                print(student[0]) will print "Sandip"
                student[0] = "Rupam" this statement will overwrite at 0th index and replace "Sandip" to "Rupam"
                print(student[0]) will now print "Rupam"
In Python 
    String -> immutable
    List   -> mutable

"""
# List of same data type
mark = [98,94,99,91]

print(mark)
print(type(mark))

print(mark[0])
print(mark[1])
print(mark[2])
print(mark[3])

# List of different types of data type

student = ["Sandip",20,56.96,"Maity"]

print(student)
print(type(student))

print(student[0])
print(student[1])
print(student[2])
print(student[3])

