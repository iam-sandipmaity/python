# WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. Use subjects name as key & makes as value

marks = {}

x = int(input("Enter phy : "))
marks.update({"phy" : x})
x = int(input("Enter math : "))
marks.update({"math" : x})
x = int(input("Enter chem : "))
marks.update({"chem" : x})

print(marks)