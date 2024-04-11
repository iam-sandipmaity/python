"""
Operator and Their Types

    a + b 
     in this expression "a" and "b" are called operand and "+" is operator

    1> Arithmatic Operator (+ , - , * , / , % , **)
    2> Relational Operator (== , != , < , <= , > , >=)
    3> Assignment Operator (= , += , -= , *= , /= , **=)
    4> Logical Operator (not , or , and)

"""

#1> Arithmatic Operator (+ , - , * , / , % , **)

a,b = 5,2
print("a = ",a," b = ",b)
print("a + b = ",a+b," a - b = ",a-b, " a * b = ",a*b," a / b = ",a/b," a % b = ",a%b," a ** b = ",a**b)

# 2> Relational/ comparison Operator (== , != , < , <= , > , >=)

print(a==b)  #F
print(a!=b)  #T
print(a<b)   #F
print(a<=b)  #F
print(a>b)   #T
print(a>=b)  #T


# 3> Assignment Operator (= , += , -= , *= , /= , **=)

num = 15
num += 5 # 15 + 5 = 20
print(num)
num -= 5 # 20 - 5 = 15
print(num)
num *= 5 # 15 * 5 = 75
print(num)
num /= 5 # 75 / 5 = 15.0
print(num)
num **= 5 # 15.0^5 = 759375.0
print(num)


#4> Logical Operator (not , or , and)

print(not(True))
print(not(False))
print((False or False) and (False or True))
print(not((False or False) and (False or True)))