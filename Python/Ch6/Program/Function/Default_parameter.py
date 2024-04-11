""" 
Default Parameter

    Assigning a default value to parameter, which is used when no argument is passed


"""

# 1
def sum(a = 2,b = 5):
    print(a+b)
sum()        #7
sum(10,45)   #55
# If we didn't put any input then functoin will take it's default input value 


# 2


# def sum(a = 2,b):
#     print(a+b)
# sum(3)

# it will return an error as always last parameter have to a default value in the default parameter case.


# 3

def sum(a, b = 5):
    print(a+b)
sum(3)      #8
sum(13,16)  #29
# In this case last parameter have a default value and first one doesn't have and if user input only 1 number, then first parameter will take user input and 2nd parameter will take the default input of b


# 4
def sum1(a,b,c,d):
    print(a+b+c+d)

sum1(1,2,3,4)   #10


def sum(a,b,c,d=6):
    print(a+b+c+d)

sum(2,3,4)  #15


def sum(a,b,c=9,d=3):
    print(a+b+c+d)

sum(3,4)    #19


def sum(a,b=8,c=56,d=10):
    print(a+b+c+d)

sum(4)     # 78







