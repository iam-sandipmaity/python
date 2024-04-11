"""
Dictionary methods :- 


    There are lots of inbuilt dictionary  Methods available.. 
    Some important methods are 

        1-> mydict.keys()    return all keys
        2-> mydict.values()  return all values
        3-> mydict.items()   returns all (key , value) pairs as tuple
        4-> mydict.get(key)  returns all the key according to value
        5-> mydict.update(newDict)  inserts the specified items to the dictionary


            ex:- student = {
                    "name" : "Sandip Maity",
                    "age"  : 20,
                    "details" : {
                        "father" : "sa",
                        "School" : "Kanpur"
                    }
                }


       1-> mydict.get("key") and mydict["key"]  both returns the key value. but, then why we should use mydict.get("key") function?

            Answere is very simple, if we working on a big programing project and if we call a key that doesn't eist in the dictionary, then the mydict["key"] will  return an error but, mydict.get("key") will return only "None" , so  avoide error statement we use mydict.get("key") fuction.

            print(student["name"])  -> 'Sandip Maity'
            print(student.get("name"))  -> 'Sandip Maity'

            print(student["address"])  -> return an error
            print(student.get("address"))  -> None



       2-> mydict.keys()  only return keys value not nested keys value.

        print(student.keys())  -> dict_keys(['name', 'age', 'details'])
            
            ->list(mydict.keys())  by this way we can easily type cast dictionary values list to a normal list form.

                print(list(student.keys()))  -> ['name', 'age', 'details']


    3-> mydict.values()  returns all values with nested loop values also

        print(student.values())  -> dict_values(['Sandip Maity', 20, {'father': 'sa', 'School': 'Kanpur'}])

        print(list(student.values())) -> ['Sandip Maity', 20, {'father': 'sa', 'School': 'Kanpur'}]

   

"""



student = {
    "name" : "Sandip Maity",
    "age"  : 20,
    "details" : {
        "father" : "sa",
        "School" : "Kanpur"
    }
}


# 1

print(student["name"])  #-> 'Sandip Maity'
print(student.get("name"))  #-> 'Sandip Maity'

# print(student["address"])  #-> return an error
print(student.get("address"))  #-> None


# 2

print(student.keys())  #-> dict_keys(['name', 'age', 'details'])
print(list(student.keys()))  #-> ['name', 'age', 'details']


# 3

print(student.values()) 
print(list(student.values())) 

# 4

print(student.items())  #dict_items([('name', 'Sandip Maity'), ('age', 20), ('details', {'father': 'sa', 'School': 'Kanpur'})])


# 5

print(student.get("name"))   # 'Sandip Maity'
print(student.get("address"))   #  None

# 6

new_dict = {"city" : "kolkata", "school" : "kanpur", "age" : 19}

student.update(new_dict)
print(student)

"""
{'name': 'Sandip Maity', 'age': 19, 'details': {'father': 'sa', 'School': 'Kanpur'}, 'city': 'kolkata', 'school': 'kanpur'}
"""

student.update({"nation" : "India" , "age" : 21})
print(student)

"""
{'name': 'Sandip Maity', 'age': 21, 'details': {'father': 'sa', 'School': 'Kanpur'}, 'city': 'kolkata', 'school': 'kanpur', 'nation': 'India'}
"""