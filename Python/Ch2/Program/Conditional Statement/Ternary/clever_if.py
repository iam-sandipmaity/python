"""

clever if syntax :- 

    <var> = (false_value,true_value) [<condition>]

"""

# 18 years older or more can vote
age = int(input("Enter Your Age : "))

vote = ("NO","YES") [age >= 18]
print(vote)
