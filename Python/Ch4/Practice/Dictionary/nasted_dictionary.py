"""
Nasted Dictionary

    dict = {
        "value" : "keys",
        "nasted_dictionary" : {
            "key1" : "val1",
            "key2" : "val2",
            "key3" : "val3",
            "Key4" : {
                "key5" : "val5",
                "key6" : "val6"
            }
        }
    }

"""

student = {
    "first_name" : "Sandip",
    "last_name"  : "Maity",
    "details"    :  {
        "age" : 20,
        "father" : "Sanatan",
        "mother" : "Dipali",
        "haveBankAc" : True,
        "Address" : {
            "village" : "Kanpur",
            "post"    : "Patashpur",
            "dist"    : "Purba Medinipur" or "East Midnapore",
            "state"   : "West Bengal",
        },
        "Academic" : {

            "Education" : "Secondary" and "Higher Secondary" and "post Graduation" ,
            "Secondary" : "General",
            "Higher Secondary" : "Science",
            "Post Graduatioin" : {
                "B.Tech" : "ECE",
                "College": "TECB", 
            }
        }
    }
}

print(student)
print(student["first_name"])
print(student["details"])
print(student["details"]["Address"])
print(student["details"]["Academic"])
print(type(student))
print(type(student["details"]))

print(student["details"]["Academic"]["Post Graduatioin"]["B.Tech"])


""""
Output Screen

{'first_name': 'Sandip', 'last_name': 'Maity', 'details': {'age': 20, 'father': 'Sanatan', 'mother': 'Dipali', 'haveBankAc': True, 'Address': {'village': 'Kanpur', 'post': 'Patashpur', 'dist': 'Purba Medinipur', 'state': 'West Bengal'}, 'Academic': {'Education': 'post Graduation', 'Secondary': 'General', 'Higher Secondary': 'Science', 'Post Graduatioin': {'B.Tech': 'ECE', 'College': 'TECB'}}}}
Sandip
{'age': 20, 'father': 'Sanatan', 'mother': 'Dipali', 'haveBankAc': True, 'Address': {'village': 'Kanpur', 'Academic': {'Education': 'post Graduation', 'Secondary': 'General', 'Higher Secondary': 'Science', 'Post Graduatioin': {'B.Tech': 'ECE', 'College': 'TECB'}}}
{'village': 'Kanpur', 'post': 'Patashpur', 'dist': 'Purba Medinipur', 'state': 'West Bengal'}
{'Education': 'post Graduation', 'Secondary': 'General', 'Higher Secondary': 'Science', 'Post Graduatioin': {'B.Tech': 'ECE', 'College': 'TECB'}}
<class 'dict'>
<class 'dict'>
ECE
"""