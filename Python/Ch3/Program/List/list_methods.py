"""
List Functions:

list = [1,9,3]
    There are many inbuid string function is available. But we are going to face some most usefull functions

        1> list.append(el)  adds an element at the end [1,9,3,el]
        2> list.sort()      Sort in ascendind order [1,3,9]
        3> list.reverse()   reverse any list [1,9,3] -> [3,9,1]
        4> list.sort(reverse = True) reverse in decending order [1,9,3] -> [9,3,1]
        5> list.insert(idx,el) insert element at particuler index
        6> list.remove(element)  remove first occurence of the element
        7> list.pop(idx)    removes element at index

        etc...

"""

mark = [56,89,75,63,45,21]

print(mark)
print(type(mark))

mark.append(32)   
print(mark)

mark.sort()
print(mark)

mark.reverse()
print(mark)

mark.sort(reverse=True)
print(mark)

mark.insert(7,633)
print(mark)

mark.insert(70,8285)  # index 70 is biger than available index total 8. So it take last index
print(mark)

mark.remove(56)
print(mark)

mark.pop(2)
print(mark)


"""
Total Output Screen is 


[56, 89, 75, 63, 45, 21]
<class 'list'>
[56, 89, 75, 63, 45, 21, 32]
[21, 32, 45, 56, 63, 75, 89]
[89, 75, 63, 56, 45, 32, 21]
[89, 75, 63, 56, 45, 32, 21]
[89, 75, 63, 56, 45, 32, 21, 633]
[89, 75, 63, 56, 45, 32, 21, 633, 8285]       
[89, 75, 63, 45, 32, 21, 633, 8285]
[89, 75, 45, 32, 21, 633, 8285]

"""