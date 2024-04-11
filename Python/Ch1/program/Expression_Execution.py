"""
Expresion Execution

    1> String and Numaric values can operate together with *

    2> String and String can operate with +

    3> Numeric values can operate with all arithmatic oeration (+,-,*,/,%,**)

    4> Arithmatic  operation with integer and float will result in float

        int (+,-,*) int = int
        int / int = float
        int (+,-,*,/) float = float
        float (+,-,*,/) int = float
        float (+,-,/,)* float = float

    5> Division of 2 integer will be always float ( 1/2 = 0.5   int/int = float)

        1/2 = 0.5
        8/4 = 2.0
        5/2 = 2.5

    6> Integer Division with float and int will give int (//)

        1//2 = 0  
        8//4 = 2
        5//2 = 2

        Result of A//B is same as floor(A/B)
         floor(number) -> cloosest less or same integer

         Ex:- 
         12//5 = 2 (12/5=2.2->2)
         -12//5 = -3 (-12/5 = -2.2 -> -3)

         floor of any number
         0.1 -> 0
         5.2 -> 5
         7.99 -> 7
         -5.2 -> -6
         -4.99 -> -5
         -3.01 -> -4

    7> Remainder is negative when denominator is nagative
        numenator     denominator   result
          +ve           +ve          +ve
          +ve           -ve          -ve
          -ve           +ve          +ve
          -ve           -ve          -ve

                 5  %   2  =  1
                 5  %  -2  = -1
                -5  %   2  =  1
                -5  %  -2  = -1


"""

# 1
A,B = 2,3
Txt = "@"
print(A*Txt*B)

"""
It gives a output of @@@@@@ 
    in String and integer multipication, String repeat itself by the integer number

    in this case A*B = 2*3 = 6, so 6 time @ repeat itself
"""

#2
C,D = "2",3
Txt = "@"
print((C+Txt)*D)
"""
It gives a output of 2@2@2@ 
    Here 2 string concatenate them and then they repeat them multiple of the integer D or 3 times
"""

#3
val1 = 5
val2 = 2
print("val1 = ",val1," val2 = ", val2)
print("sum = ",val1+val2, " diff =  ",val1-val2, " mul =  ",val1*val2 , " div =  ",val1/val2," mod =  ",val1%val2," power =  ", val1**val2)


#4
num1 = 2
num2 = 3.5

print("num1 = ",num1," num2 = ",num2)
print("sum = ",num1+num2, " diff =  ",num1-num2, " mul =  ",num1*num2 , " div =  ",num1/num2," mod =  ",num1%num2," power =  ", num1**num2)

#5
n1 = 1
n2 = 2
print (n1/n2)

#6
print(n1//n2)
print(type(n1//n2))


#7

print(5 % 2)     #1
print(5 % -2)    #-1
print(-5 % 2)    #1
print(-5 % -2)   #-1


""""
Full output Screen


@@@@@@

2@2@2@

val1 =  5  val2 =  2
sum =  7  diff =   3  mul =   10  div =   2.5  mod =   1  power =   25

num1 =  2  num2 =  3.5        
sum =  5.5  diff =   -1.5  mul =   7.0  div =   0.5714285714285714  mod =   2.0  power =   11.313708498984761

0.5

0
<class 'int'>

1
-1
1
-1
"""

